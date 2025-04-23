import aws_cdk as core
import aws_cdk.assertions as assertions

from searxng_deploy.searxng_deploy_stack import SearxngDeployStack

# example tests. To run these tests, uncomment this file along with the example
# resource in searxng_deploy/searxng_deploy_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SearxngDeployStack(app, "searxng-deploy")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
