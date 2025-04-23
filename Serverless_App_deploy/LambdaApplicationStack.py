import os
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda,
    aws_iam as iam,
    CfnOutput,
)
from constructs import Construct

class LambdaApplicationStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # 从 context 读取 main_url
        self.main_url = self.node.try_get_context('main_url')
        
        # 获取当前区域
        current_region = Stack.of(self).region
        

        # 构建并推送镜像到 ECR
        ecr_image = aws_lambda.EcrImageCode.from_asset_image(
            directory=os.path.join(os.getcwd(), "app_docker")
        )

        # 创建 Lambda 函数
        myfunc = aws_lambda.Function(
            self, "lambdaContainerFunction",
            description="Lambda Container Function",
            code=ecr_image,
            handler=aws_lambda.Handler.FROM_IMAGE,
            runtime=aws_lambda.Runtime.FROM_IMAGE,
            function_name=f"LambdaApplication-function-{current_region}",
            memory_size=128,
            reserved_concurrent_executions=10,
            timeout=Duration.seconds(120)
        )

        # 添加权限
        myfunc_role = myfunc.role
        myfunc_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
        )

        # 添加 Lambda 权限
        aws_lambda.CfnPermission(self, "MyCfnPermission1",
            action="lambda:InvokeFunctionUrl",
            function_name=myfunc.function_name,
            principal="edgelambda.amazonaws.com",
            function_url_auth_type="AWS_IAM"
        )
        aws_lambda.CfnPermission(self, "MyCfnPermission2",
            action="lambda:InvokeFunctionUrl",
            function_name=myfunc.function_name,
            principal="cloudfront.amazonaws.com",
            function_url_auth_type="AWS_IAM"
        )

        # 添加函数 URL
        function_url = myfunc.add_function_url(
            auth_type=aws_lambda.FunctionUrlAuthType.AWS_IAM,
            invoke_mode=aws_lambda.InvokeMode.BUFFERED
        )
        
        # 输出函数 URL
        CfnOutput(self, "LambdaApplication-function-url", value=function_url.url)
        
        # 暴露函数 URL 供其他 stack 使用
        self.function_url = function_url.url


