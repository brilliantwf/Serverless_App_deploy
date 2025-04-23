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
            hosted_zone = route53.HostedZone.from_lookup(
                self, "ExistingHostedZone",
                domain_name=domain_name
            )
        except Exception:
            # 如果托管区不存在，则创建新的
            hosted_zone = route53.PublicHostedZone(
                self, "LambdaApplicationHostedZone",
                zone_name=domain_name,
                comment="Hosted zone for LambdaApplication latency-based routing"
            )

        # 为每个区域的 Lambda URL 创建记录
        for region, stack in LambdaApplicationStack_stacks.items():
            # 创建延迟路由记录
            route53.CnameRecord(
                self, f"LatencyRecord-{region}",
                zone=hosted_zone,
                record_name=custom_origin,
                domain_name=stack.function_url.replace("https://", ""),  # 使用 Lambda URL
                region=region  # 设置区域即可启用延迟路由
            )

        # 输出托管区 ID
        CfnOutput(self, "HostedZoneId", value=hosted_zone.hosted_zone_id) 