from aws_cdk import App
from Serverless_App_deploy.LambdaApplicationStack import LambdaApplicationStack
from Serverless_App_deploy.CloudfrontStack import CloudfrontStack
from Serverless_App_deploy.route53_stack import Route53Stack

app = App()

# 从 CDK context 获取部署配置
LambdaApplicationStack_regions = app.node.try_get_context('LambdaApplicationStack_regions') or ["us-west-2"]
edgelambda_region = app.node.try_get_context('edgelambda_region') or "us-east-1"
# 存储所有创建的 LambdaApplicationStack 用于后续引用
LambdaApplicationStack_stacks = {}

# 在多个区域部署 LambdaApplicationStack
for region in LambdaApplicationStack_regions:
    env = {'region': region}
    stack_name = f"LambdaApplicationStack-{region}"
    stack = LambdaApplicationStack(
        app, 
        stack_name, 
        env=env,
        cross_region_references=True
    )
    LambdaApplicationStack_stacks[region] = stack

# 在指定区域部署 EdgelambdaStack
edgelambda_env = {'region': edgelambda_region}
cloudfront_stack = CloudfrontStack(
    app, 
    "CloudfrontStack", 
    LambdaApplicationStack=LambdaApplicationStack,  # 使用相同区域的 APP stack
    env=edgelambda_env,
    cross_region_references=True
)
# 部署 Route53 Stack
route53_stack = Route53Stack(
    app,
    "Route53Stack",
    LambdaApplicationStack_stacks=LambdaApplicationStack_stacks,
    env={'region': edgelambda_region},
    cross_region_references=True
)

app.synth()