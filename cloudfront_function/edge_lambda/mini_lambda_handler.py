import json
import base64
from botocore.awsrequest import AWSRequest
from botocore.auth import SigV4Auth
import botocore.session
import urllib.parse
import re
from urllib.parse import parse_qsl

session = botocore.session.Session()


def signed_request(event, context={}):
    print("event=" + json.dumps(event), flush=True)

    request = event['Records'][0]['cf']['request']

    # change the origin
    target_origin = (
        event.get("Records", [{}])[0]
        .get("cf", {})
        .get("request", {})
        .get("origin", {})
        .get("custom", {})
        .get("customHeaders", {})
        .get("target_origin", [{}])[0]  # 假设标头存在且至少有一个值
        .get("value", "默认值或None")
    )
    print("target_origin=" + target_origin, flush=True)
    request['headers']['host'][0]['value'] = target_origin
    request['origin']['custom']['domainName'] = target_origin

    headers = request['headers']

    # remove the x-forwarded-for from the signature
    del headers['x-forwarded-for']

    headers = {v[0]['key']: v[0]['value'] for k, v in headers.items()}

    host = request['headers']['host'][0]['value']
    region = host.split(".")[2]

    # build the request to sign
    req = AWSRequest(
        method=request['method'],
        url=request['uri'],
        params=parse_qsl(request['querystring'], keep_blank_values=True) if 'querystring' in request and request['querystring'] else None,
        data=base64.b64decode(request['body']['data']) if 'body' in request and 'data' in request['body'] else None,
        headers=headers
    )
    req.context['signing'] = {'signing_name': 'lambda', 'region': region}
    SigV4Auth(session.get_credentials(), 'lambda', region).add_auth(req)

    # reformat the headers for CloudFront
    request['headers'] = {
        header.lower(): [{'key': header, 'value': value}]
        for header, value in req.headers.items()
    }

    print("signedRequest=" + json.dumps(request), flush=True)
    return request


def lambda_handler(event, context):
   return signed_request(event, context)