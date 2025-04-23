from aws_cdk import (
    Duration,
    Stack,
    Environment,
    aws_lambda,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_iam as iam,
    CfnOutput,
)
from constructs import Construct
from Serverless_App_deploy.LambdaApplicationStack import LambdaApplicationStack
class CloudfrontStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, LambdaApplicationStack: LambdaApplicationStack, **kwargs) -> None:
        # 获取 需要部署的region
        edgelambda_region = scope.node.try_get_context('edgelambda_region')
        if not edgelambda_region:
            raise ValueError("No edgelambda_region specified in cdk.context.json")
            
        # 设置环境并启用跨区域引用
        kwargs['env'] = Environment(region=edgelambda_region)
        kwargs['cross_region_references'] = True
        
        super().__init__(scope, construct_id, **kwargs)
        
        self._region = edgelambda_region
        
        edge_lambda_role = iam.Role(self, "edge_lambda_role",
            assumed_by=iam.CompositePrincipal(
                iam.ServicePrincipal("edgelambda.amazonaws.com"),
                iam.ServicePrincipal("lambda.amazonaws.com")
            )
        )

        edge_lambda_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaRole"))
        ## signv4 lambda deployment
        edgelambda = aws_lambda.Function(self, "edgelambda",
            code=aws_lambda.Code.from_asset("cloudfront_function/edge_lambda"),
            handler="auth_lambda_handler.lambda_handler",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            role=edge_lambda_role,
            timeout=Duration.seconds(10)
        )
        edge_lambda_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"))
        edge_lambda_role.attach_inline_policy(iam.Policy(self, "invokelambdaurl",
            statements=[
                iam.PolicyStatement(
                    effect=iam.Effect.ALLOW,
                    actions=["lambda:InvokeFunctionUrl"],
                    resources=["*"]
                )
            ]
        ))
        custom_origin = self.node.try_get_context('custom_origin')
        if not custom_origin:
            raise ValueError("No custom_origin specified in cdk.context.json")
        ## cloudfront distribution
        CloudfrontStack_distribution = cloudfront.Distribution(self, "CloudfrontStack-distribution",
            default_behavior=cloudfront.BehaviorOptions(
                compress=True,
                cache_policy=cloudfront.CachePolicy.CACHING_DISABLED,
                allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL,
                origin_request_policy=cloudfront.OriginRequestPolicy.ALL_VIEWER,
                origin=origins.HttpOrigin(domain_name=custom_origin,custom_headers={"TARGET_ORIGIN":self.node.try_get_context('custom_origin')}),
                edge_lambdas=[cloudfront.EdgeLambda(
                    function_version=edgelambda.current_version,
                    event_type=cloudfront.LambdaEdgeEventType.ORIGIN_REQUEST,
                    include_body=True
                )]
            )
        ) 

        CfnOutput(self, "CloudfrontStack-distribution-url", value="https://"+CloudfrontStack_distribution.domain_name)