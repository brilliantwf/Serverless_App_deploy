import json
import time
import logging
import base64
from typing import Dict, Tuple, Optional
from urllib.parse import urlparse
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import botocore.session
import socket
from functools import lru_cache
# Constants
TTL = 300  # DNS cache time in seconds
#DEFAULT_DNS_HOST = 'latency.1372020.xyz'
# Logging setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.getLogger('botocore').setLevel(logging.ERROR)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
# Type aliases and global variables
DNSCache = Dict[str, Tuple[str, float]]
dns_cache: DNSCache = {}
session = botocore.session.Session()
@lru_cache(maxsize=128)
def get_cname(host: str) -> Optional[str]:
    try:
        result = socket.gethostbyname_ex(host)
        return result[0] if result[0] != host else None
    except socket.gaierror as e:
        logger.error(f"DNS resolution error for {host}: {e}")
    return None
def get_best_lambda_url(dns_host: str) -> str:
    now = time.time()
    if dns_host in dns_cache and now < dns_cache[dns_host][1]:
        return dns_cache[dns_host][0]
    cname = get_cname(dns_host)
    logger.info(f"DNS cache miss, resolving {dns_host}")
    if cname:
        dns_cache[dns_host] = (cname, now + TTL)
        return cname
    return dns_host
def sign_request(request: Dict, target_domain: str) -> Tuple[Dict, str]:
    headers = {v[0]['key']: v[0]['value'] for k, v in request['headers'].items() if k != 'x-forwarded-for'}
    path = request['uri']
    if querystring := request.get('querystring'):
        path += f"?{querystring}"
    url = f"https://{target_domain}{path}"
    body = base64.b64decode(request['body']['data']) if 'body' in request and 'data' in request['body'] else None
    aws_request = AWSRequest(method=request['method'], url=url, data=body, headers=headers)
    region = urlparse(url).hostname.split('.')[2]
    aws_request.context['signing'] = {'signing_name': 'lambda', 'region': region}
    SigV4Auth(session.get_credentials(), 'lambda', region).add_auth(aws_request)
    # signed_url = aws_request.url
    # logger.info(f"Signed URL: {signed_url}")
    request['headers'] = {header.lower(): [{'key': header, 'value': value}] for header, value in aws_request.headers.items()}
    return request
def lambda_handler(event: Dict, context) -> Dict:
    try:
        request = event['Records'][0]['cf']['request']
        original_origin = request.get('origin', {}).get('custom', {})
        custom_headers = request['origin']['custom']['customHeaders']
        # dns_host = custom_headers.get('target_origin', [{'value': DEFAULT_DNS_HOST}])[0]['value']
        if 'target_origin' not in custom_headers:
            raise ValueError("Missing required custom header: target_origin")
        dns_host = custom_headers['target_origin'][0]['value']
        target_domain = get_best_lambda_url(dns_host)
        logger.info(json.dumps({
            "message": "Request info",
            "ip": request['clientIp'],
            "country": request['headers'].get('cloudfront-viewer-country', [{'value': 'Unknown'}])[0]['value'],
            "dns_host": dns_host,
            "uri": request['uri'],
            "best_lambda": target_domain
        }))
        if target_domain:
            request['origin'] = {
                'custom': {
                    'domainName': target_domain,
                    'port': original_origin.get('port', 443),
                    'protocol': original_origin.get('protocol', 'https'),
                    'sslProtocols': original_origin.get('sslProtocols', ['TLSv1.2']),
                    'path': original_origin.get('path', ''),
                    'readTimeout': original_origin.get('readTimeout', 30),
                    'keepaliveTimeout': original_origin.get('keepaliveTimeout', 10),
                    'customHeaders': original_origin.get('customHeaders', {})
                }
            }
            request['headers']["host"] = [{'key': "host", 'value': target_domain}]
            request = sign_request(request, target_domain)
        else:
            logger.error("Failed to resolve Lambda URL, using original request")
    except KeyError as e:
        logger.error(f"Missing key in event structure: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise
    return request
if __name__ == "__main__":
    with open('test_event.json', 'r') as f:
        test_event = json.load(f)
    class LambdaContext:
        def __init__(self):
            self.function_name = "test_function"
            self.function_version = "$LATEST"
            self.invoked_function_arn = "arn:aws:lambda:us-east-1:123456789012:function:test_function"
    result = lambda_handler(test_event, LambdaContext())