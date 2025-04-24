from aws_cdk import (
    Stack,
    aws_route53 as route53,
    CfnOutput,
)
from constructs import Construct
from urllib.parse import urlparse

class Route53Stack(Stack):
    def __init__(self, scope: Construct, id: str, LambdaApplicationStack_stacks: dict, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # 从 context 获取 custom_origin
        custom_origin = self.node.try_get_context('custom_origin')
        if not custom_origin:
            raise ValueError("No custom_origin specified in cdk.context.json")

        # 提取主域名部分
        parsed_url = urlparse(f"https://{custom_origin}")
        domain_parts = parsed_url.netloc.split('.')
        if len(domain_parts) >= 2:
            domain_name = '.'.join(domain_parts[-2:])  # 获取最后两部分作为主域名
        else:
            raise ValueError(f"Invalid domain format: {custom_origin}")

        # 尝试查找已存在的托管区
        try:
            # 从 context 获取托管区域 ID
            hosted_zone_id = self.node.try_get_context('hosted_zone_id')
            if not hosted_zone_id:
                raise ValueError("No hosted_zone_id specified in cdk.context.json")

            # 使用托管区域 ID 直接引用
            hosted_zone = route53.HostedZone.from_hosted_zone_attributes(
                self, "ExistingHostedZone",
                hosted_zone_id=hosted_zone_id,
                zone_name=domain_name
            )
            
            print(f"Using existing hosted zone: {hosted_zone.hosted_zone_id}")
            
        except Exception as e:
            print(f"Error looking up hosted zone: {str(e)}")
            # 如果查找失败，创建新的托管区域
            hosted_zone = route53.HostedZone(
                self, "NewHostedZone",
                zone_name=domain_name
            )
            print(f"Created new hosted zone: {hosted_zone.hosted_zone_id}")

        # 为每个区域的 Lambda URL 创建记录
        for region, stack in LambdaApplicationStack_stacks.items():
            # 打印调试信息
            print(f"Processing region: {region}")
            print(f"Function URL: {stack.function_url}")
            
            # 直接提取域名部分（移除 https:// 和末尾的 /）
            domain_name = stack.function_url.replace('https://', '').rstrip('/')
            
            if not domain_name:
                raise ValueError(f"Invalid function URL format for region {region}: {stack.function_url}")
            
            # 创建延迟路由记录
            route53.CnameRecord(
                self, f"LatencyRecord-{region}",
                zone=hosted_zone,
                record_name=custom_origin,
                domain_name=domain_name,
                region=region
            )

        # 输出托管区 ID
        CfnOutput(self, "HostedZoneId", value=hosted_zone.hosted_zone_id) 