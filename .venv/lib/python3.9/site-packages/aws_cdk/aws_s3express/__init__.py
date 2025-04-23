r'''
# AWS::S3Express Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_s3express as s3express
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for S3Express construct libraries](https://constructs.dev/search?q=s3express)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::S3Express resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Express.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::S3Express](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Express.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnBucketPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3express.CfnBucketPolicy",
):
    '''The ``AWS::S3Express::BucketPolicy`` resource defines an Amazon S3 bucket policy to an Amazon S3 directory bucket.

    - **Permissions** - If you are using an identity other than the root user of the AWS account that owns the bucket, the calling identity must both have the required permissions on the specified bucket and belong to the bucket owner's account in order to use this operation. For more information about directory bucket policies and permissions, see `AWS Identity and Access Management (IAM) for S3 Express One Zone <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html>`_ in the *Amazon S3 User Guide* .

    .. epigraph::

       To ensure that bucket owners don't inadvertently lock themselves out of their own buckets, the root principal in a bucket owner's AWS account can perform the ``GetBucketPolicy`` , ``PutBucketPolicy`` , and ``DeleteBucketPolicy`` API actions, even if their bucket policy explicitly denies the root principal's access. Bucket owner root principals can only be blocked from performing these API actions by VPC endpoint policies and AWS Organizations policies.

    The required permissions for CloudFormation to use are based on the operations that are performed on the stack.

    - Create
    - s3express:GetBucketPolicy
    - s3express:PutBucketPolicy
    - Read
    - s3express:GetBucketPolicy
    - Update
    - s3express:GetBucketPolicy
    - s3express:PutBucketPolicy
    - Delete
    - s3express:GetBucketPolicy
    - s3express:DeleteBucketPolicy
    - List
    - s3express:GetBucketPolicy
    - s3express:ListAllMyDirectoryBuckets

    For more information about example bucket policies, see `Example bucket policies for S3 Express One Zone <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam-example-bucket-policies.html>`_ in the *Amazon S3 User Guide* .

    The following operations are related to ``AWS::S3Express::BucketPolicy`` :

    - `PutBucketPolicy <https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html>`_
    - `GetBucketPolicy <https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html>`_
    - `DeleteBucketPolicy <https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html>`_
    - `ListDirectoryBuckets <https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListDirectoryBuckets.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-bucketpolicy.html
    :cloudformationResource: AWS::S3Express::BucketPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3express as s3express
        
        # policy_document: Any
        
        cfn_bucket_policy = s3express.CfnBucketPolicy(self, "MyCfnBucketPolicy",
            bucket="bucket",
            policy_document=policy_document
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bucket: builtins.str,
        policy_document: typing.Any,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bucket: The name of the S3 directory bucket to which the policy applies.
        :param policy_document: A policy document containing permissions to add to the specified bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy `PolicyDocument <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument>`_ resource description in this guide and `Policies and Permissions in Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html>`_ in the *Amazon S3 User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7ae0c19fbf2c7c716bc3304458f2695912d196d3e7439999f721b69fdbfc5a0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBucketPolicyProps(bucket=bucket, policy_document=policy_document)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0da69b8aee8ed367e63ca61c9ad9c6ce2b5fd2aff3c02cb553118847c89867c)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a427439734058e5e6251cd5c0aaeed7ade47e92954992912236d939d3b496350)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        '''The name of the S3 directory bucket to which the policy applies.'''
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dedf6ffab37d96f5ca0d97fbcb6904b8dc185fd26912baba5f2b683aec30a5e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''A policy document containing permissions to add to the specified bucket.'''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__575ca46990b1014411a210bab87827014d15a4bd9119ec2a06a134d0e642cfff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3express.CfnBucketPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "policy_document": "policyDocument"},
)
class CfnBucketPolicyProps:
    def __init__(self, *, bucket: builtins.str, policy_document: typing.Any) -> None:
        '''Properties for defining a ``CfnBucketPolicy``.

        :param bucket: The name of the S3 directory bucket to which the policy applies.
        :param policy_document: A policy document containing permissions to add to the specified bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy `PolicyDocument <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument>`_ resource description in this guide and `Policies and Permissions in Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html>`_ in the *Amazon S3 User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-bucketpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3express as s3express
            
            # policy_document: Any
            
            cfn_bucket_policy_props = s3express.CfnBucketPolicyProps(
                bucket="bucket",
                policy_document=policy_document
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7978963298afc97ec8564e6e114bf73c7797f21fb71f9d0a187dd5852499f423)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "policy_document": policy_document,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''The name of the S3 directory bucket to which the policy applies.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-bucketpolicy.html#cfn-s3express-bucketpolicy-bucket
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''A policy document containing permissions to add to the specified bucket.

        In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy `PolicyDocument <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument>`_ resource description in this guide and `Policies and Permissions in Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html>`_ in the *Amazon S3 User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-bucketpolicy.html#cfn-s3express-bucketpolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBucketPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDirectoryBucket(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3express.CfnDirectoryBucket",
):
    '''The ``AWS::S3Express::DirectoryBucket`` resource defines an Amazon S3 directory bucket in the same AWS Region where you create the AWS CloudFormation stack.

    To control how AWS CloudFormation handles the bucket when the stack is deleted, you can set a deletion policy for your bucket. You can choose to *retain* the bucket or to *delete* the bucket. For more information, see `DeletionPolicy attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html>`_ .
    .. epigraph::

       You can only delete empty buckets. Deletion fails for buckets that have contents.

    - **Permissions** - The required permissions for CloudFormation to use are based on the operations that are performed on the stack.
    - Create
    - s3express:CreateBucket
    - s3express:ListAllMyDirectoryBuckets
    - Read
    - s3express:ListAllMyDirectoryBuckets
    - ec2:DescribeAvailabilityZones
    - Delete
    - s3express:DeleteBucket
    - s3express:ListAllMyDirectoryBuckets
    - List
    - s3express:ListAllMyDirectoryBuckets
    - PutBucketEncryption
    - s3express:PutEncryptionConfiguration
    - To set a directory bucket default encryption with SSE-KMS, you must also have the kms:GenerateDataKey and kms:Decrypt permissions in IAM identity-based policies and AWS KMS key policies for the target AWS KMS key.
    - GetBucketEncryption
    - s3express:GetBucketEncryption
    - DeleteBucketEncryption
    - s3express:PutEncryptionConfiguration

    The following operations are related to ``AWS::S3Express::DirectoryBucket`` :

    - `CreateBucket <https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html>`_
    - `ListDirectoryBuckets <https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListDirectoryBuckets.html>`_
    - `DeleteBucket <https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html
    :cloudformationResource: AWS::S3Express::DirectoryBucket
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3express as s3express
        
        cfn_directory_bucket = s3express.CfnDirectoryBucket(self, "MyCfnDirectoryBucket",
            data_redundancy="dataRedundancy",
            location_name="locationName",
        
            # the properties below are optional
            bucket_encryption=s3express.CfnDirectoryBucket.BucketEncryptionProperty(
                server_side_encryption_configuration=[s3express.CfnDirectoryBucket.ServerSideEncryptionRuleProperty(
                    bucket_key_enabled=False,
                    server_side_encryption_by_default=s3express.CfnDirectoryBucket.ServerSideEncryptionByDefaultProperty(
                        sse_algorithm="sseAlgorithm",
        
                        # the properties below are optional
                        kms_master_key_id="kmsMasterKeyId"
                    )
                )]
            ),
            bucket_name="bucketName",
            lifecycle_configuration=s3express.CfnDirectoryBucket.LifecycleConfigurationProperty(
                rules=[s3express.CfnDirectoryBucket.RuleProperty(
                    status="status",
        
                    # the properties below are optional
                    abort_incomplete_multipart_upload=s3express.CfnDirectoryBucket.AbortIncompleteMultipartUploadProperty(
                        days_after_initiation=123
                    ),
                    expiration_in_days=123,
                    id="id",
                    object_size_greater_than="objectSizeGreaterThan",
                    object_size_less_than="objectSizeLessThan",
                    prefix="prefix"
                )]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        data_redundancy: builtins.str,
        location_name: builtins.str,
        bucket_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDirectoryBucket.BucketEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDirectoryBucket.LifecycleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_redundancy: The number of Zone (Availability Zone or Local Zone) that's used for redundancy for the bucket.
        :param location_name: The name of the location where the bucket will be created. For directory buckets, the name of the location is the Zone ID of the Availability Zone (AZ) or Local Zone (LZ) where the bucket will be created. An example AZ ID value is ``usw2-az1`` .
        :param bucket_encryption: Specifies default encryption for a bucket using server-side encryption with Amazon S3 managed keys (SSE-S3) or AWS KMS keys (SSE-KMS). For information about default encryption for directory buckets, see `Setting and monitoring default encryption for directory buckets <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-bucket-encryption.html>`_ in the *Amazon S3 User Guide* .
        :param bucket_name: A name for the bucket. The bucket name must contain only lowercase letters, numbers, and hyphens (-). A directory bucket name must be unique in the chosen Zone (Availability Zone or Local Zone). The bucket name must also follow the format ``*bucket_base_name* -- *zone_id* --x-s3`` (for example, ``*bucket_base_name* -- *usw2-az1* --x-s3`` ). If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. For information about bucket naming restrictions, see `Directory bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html>`_ in the *Amazon S3 User Guide* . .. epigraph:: If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.
        :param lifecycle_configuration: Container for lifecycle rules. You can add as many as 1000 rules. For more information see, `Creating and managing a lifecycle configuration for directory buckets <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-lifecycle.html>`_ in the *Amazon S3 User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea5a1e5897b0467fb93393ad6ea2dbcd3916f27713079e8bef3badf71ce2bb20)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDirectoryBucketProps(
            data_redundancy=data_redundancy,
            location_name=location_name,
            bucket_encryption=bucket_encryption,
            bucket_name=bucket_name,
            lifecycle_configuration=lifecycle_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61d4c01a14f34a0546048356b166c111adde5de129e3d0580f9ce73d26da1587)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09d4f293955716375e6177306d2bdfa8106614896e901a12247190cc871e9e61)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the specified bucket.

        Example: ``arn:aws:s3express: *us-west-2* : *account_id* :bucket/ *bucket_base_name* -- *usw2-az1* --x-s3``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAvailabilityZoneName")
    def attr_availability_zone_name(self) -> builtins.str:
        '''Returns the code for the Availability Zone or the Local Zone where the directory bucket was created.

        Example value for an Availability Zone code: *us-east-1f*
        .. epigraph::

           An Availability Zone code might not represent the same physical location for different AWS accounts. For more information, see `Availability Zones and Regions <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Endpoints.html>`_ in the *Amazon S3 User Guide* .

        :cloudformationAttribute: AvailabilityZoneName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAvailabilityZoneName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="dataRedundancy")
    def data_redundancy(self) -> builtins.str:
        '''The number of Zone (Availability Zone or Local Zone) that's used for redundancy for the bucket.'''
        return typing.cast(builtins.str, jsii.get(self, "dataRedundancy"))

    @data_redundancy.setter
    def data_redundancy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9234d8f5c9448b0bb44f48a13430731436331b4ef073722b1511600f9484ff5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataRedundancy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="locationName")
    def location_name(self) -> builtins.str:
        '''The name of the location where the bucket will be created.'''
        return typing.cast(builtins.str, jsii.get(self, "locationName"))

    @location_name.setter
    def location_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__352b4b43cbbf4d81310eac7a66fd236d34a92a5af6e8099d48e6ec1e7c90c7a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="bucketEncryption")
    def bucket_encryption(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDirectoryBucket.BucketEncryptionProperty"]]:
        '''Specifies default encryption for a bucket using server-side encryption with Amazon S3 managed keys (SSE-S3) or AWS KMS keys (SSE-KMS).'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDirectoryBucket.BucketEncryptionProperty"]], jsii.get(self, "bucketEncryption"))

    @bucket_encryption.setter
    def bucket_encryption(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDirectoryBucket.BucketEncryptionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec12f12e4471077fcc9afe2e16208df6b915dc349584d6784410dc28aeaa9ac3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketEncryption", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''A name for the bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__678dc679eb1daf10bbced208f7ef85b8fe01f1ae8ea62c5354ac80b289edc1ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfiguration")
    def lifecycle_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDirectoryBucket.LifecycleConfigurationProperty"]]:
        '''Container for lifecycle rules.

        You can add as many as 1000 rules.
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDirectoryBucket.LifecycleConfigurationProperty"]], jsii.get(self, "lifecycleConfiguration"))

    @lifecycle_configuration.setter
    def lifecycle_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDirectoryBucket.LifecycleConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddfd3872142b33ae9fa409c0018df1c791508213de3582b65e63e55af438eb3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfiguration", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3express.CfnDirectoryBucket.AbortIncompleteMultipartUploadProperty",
        jsii_struct_bases=[],
        name_mapping={"days_after_initiation": "daysAfterInitiation"},
    )
    class AbortIncompleteMultipartUploadProperty:
        def __init__(self, *, days_after_initiation: jsii.Number) -> None:
            '''Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before permanently removing all parts of the upload.

            For more information, see `Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Configuration <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config>`_ in the *Amazon S3 User Guide* .

            :param days_after_initiation: Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-abortincompletemultipartupload.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3express as s3express
                
                abort_incomplete_multipart_upload_property = s3express.CfnDirectoryBucket.AbortIncompleteMultipartUploadProperty(
                    days_after_initiation=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__94d67335bbcb78d0b027e59764707d68d59cd3646befac6651614e419d8af6f4)
                check_type(argname="argument days_after_initiation", value=days_after_initiation, expected_type=type_hints["days_after_initiation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "days_after_initiation": days_after_initiation,
            }

        @builtins.property
        def days_after_initiation(self) -> jsii.Number:
            '''Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-abortincompletemultipartupload.html#cfn-s3express-directorybucket-abortincompletemultipartupload-daysafterinitiation
            '''
            result = self._values.get("days_after_initiation")
            assert result is not None, "Required property 'days_after_initiation' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AbortIncompleteMultipartUploadProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3express.CfnDirectoryBucket.BucketEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "server_side_encryption_configuration": "serverSideEncryptionConfiguration",
        },
    )
    class BucketEncryptionProperty:
        def __init__(
            self,
            *,
            server_side_encryption_configuration: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDirectoryBucket.ServerSideEncryptionRuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Specifies default encryption for a bucket using server-side encryption with Amazon S3 managed keys (SSE-S3) or AWS KMS keys (SSE-KMS).

            For information about default encryption for directory buckets, see `Setting and monitoring default encryption for directory buckets <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-bucket-encryption.html>`_ in the *Amazon S3 User Guide* .

            :param server_side_encryption_configuration: Specifies the default server-side-encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-bucketencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3express as s3express
                
                bucket_encryption_property = s3express.CfnDirectoryBucket.BucketEncryptionProperty(
                    server_side_encryption_configuration=[s3express.CfnDirectoryBucket.ServerSideEncryptionRuleProperty(
                        bucket_key_enabled=False,
                        server_side_encryption_by_default=s3express.CfnDirectoryBucket.ServerSideEncryptionByDefaultProperty(
                            sse_algorithm="sseAlgorithm",
                
                            # the properties below are optional
                            kms_master_key_id="kmsMasterKeyId"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2bda13f500a0910d95ef795cf250698cc9bc399a6809500b0318dd2399fa0dfc)
                check_type(argname="argument server_side_encryption_configuration", value=server_side_encryption_configuration, expected_type=type_hints["server_side_encryption_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "server_side_encryption_configuration": server_side_encryption_configuration,
            }

        @builtins.property
        def server_side_encryption_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDirectoryBucket.ServerSideEncryptionRuleProperty"]]]:
            '''Specifies the default server-side-encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-bucketencryption.html#cfn-s3express-directorybucket-bucketencryption-serversideencryptionconfiguration
            '''
            result = self._values.get("server_side_encryption_configuration")
            assert result is not None, "Required property 'server_side_encryption_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDirectoryBucket.ServerSideEncryptionRuleProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BucketEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3express.CfnDirectoryBucket.LifecycleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"rules": "rules"},
    )
    class LifecycleConfigurationProperty:
        def __init__(
            self,
            *,
            rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDirectoryBucket.RuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Container for lifecycle rules. You can add as many as 1000 rules.

            For more information see, `Creating and managing a lifecycle configuration for directory buckets <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-lifecycle.html>`_ in the *Amazon S3 User Guide* .

            :param rules: A lifecycle rule for individual objects in an Amazon S3 Express bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-lifecycleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3express as s3express
                
                lifecycle_configuration_property = s3express.CfnDirectoryBucket.LifecycleConfigurationProperty(
                    rules=[s3express.CfnDirectoryBucket.RuleProperty(
                        status="status",
                
                        # the properties below are optional
                        abort_incomplete_multipart_upload=s3express.CfnDirectoryBucket.AbortIncompleteMultipartUploadProperty(
                            days_after_initiation=123
                        ),
                        expiration_in_days=123,
                        id="id",
                        object_size_greater_than="objectSizeGreaterThan",
                        object_size_less_than="objectSizeLessThan",
                        prefix="prefix"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__82d5e100390b1400bc989c8f7007f04e65bff5948bb5f68def580a8385603442)
                check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rules": rules,
            }

        @builtins.property
        def rules(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDirectoryBucket.RuleProperty"]]]:
            '''A lifecycle rule for individual objects in an Amazon S3 Express bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-lifecycleconfiguration.html#cfn-s3express-directorybucket-lifecycleconfiguration-rules
            '''
            result = self._values.get("rules")
            assert result is not None, "Required property 'rules' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDirectoryBucket.RuleProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LifecycleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3express.CfnDirectoryBucket.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "status": "status",
            "abort_incomplete_multipart_upload": "abortIncompleteMultipartUpload",
            "expiration_in_days": "expirationInDays",
            "id": "id",
            "object_size_greater_than": "objectSizeGreaterThan",
            "object_size_less_than": "objectSizeLessThan",
            "prefix": "prefix",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            status: builtins.str,
            abort_incomplete_multipart_upload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDirectoryBucket.AbortIncompleteMultipartUploadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            expiration_in_days: typing.Optional[jsii.Number] = None,
            id: typing.Optional[builtins.str] = None,
            object_size_greater_than: typing.Optional[builtins.str] = None,
            object_size_less_than: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies lifecycle rules for an Amazon S3 bucket.

            For more information, see `Put Bucket Lifecycle Configuration <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html>`_ in the *Amazon S3 API Reference* . For examples, see `Put Bucket Lifecycle Configuration Examples <https://docs.aws.amazon.com//AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html#API_PutBucketLifecycleConfiguration_Examples>`_ .

            You must specify at least one of the following properties: ``AbortIncompleteMultipartUpload`` , or ``ExpirationInDays`` .

            :param status: If ``Enabled`` , the rule is currently being applied. If ``Disabled`` , the rule is not currently being applied.
            :param abort_incomplete_multipart_upload: Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before permanently removing all parts of the upload.
            :param expiration_in_days: Indicates the number of days after creation when objects are deleted from Amazon S3 and Amazon S3 Glacier. If you specify an expiration and transition time, you must use the same time unit for both properties (either in days or by date). The expiration time must also be later than the transition time.
            :param id: Unique identifier for the rule. The value can't be longer than 255 characters.
            :param object_size_greater_than: Specifies the minimum object size in bytes for this rule to apply to. Objects must be larger than this value in bytes. For more information about size based rules, see `Lifecycle configuration using size-based rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html#lc-size-rules>`_ in the *Amazon S3 User Guide* .
            :param object_size_less_than: Specifies the maximum object size in bytes for this rule to apply to. Objects must be smaller than this value in bytes. For more information about sized based rules, see `Lifecycle configuration using size-based rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html#lc-size-rules>`_ in the *Amazon S3 User Guide* .
            :param prefix: Object key prefix that identifies one or more objects to which this rule applies. .. epigraph:: Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see `XML related object key constraints <https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3express as s3express
                
                rule_property = s3express.CfnDirectoryBucket.RuleProperty(
                    status="status",
                
                    # the properties below are optional
                    abort_incomplete_multipart_upload=s3express.CfnDirectoryBucket.AbortIncompleteMultipartUploadProperty(
                        days_after_initiation=123
                    ),
                    expiration_in_days=123,
                    id="id",
                    object_size_greater_than="objectSizeGreaterThan",
                    object_size_less_than="objectSizeLessThan",
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f6f9e06e8b8beb4ef85714d8e61855121cd4a13b083bc1c2de944bad75acf266)
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument abort_incomplete_multipart_upload", value=abort_incomplete_multipart_upload, expected_type=type_hints["abort_incomplete_multipart_upload"])
                check_type(argname="argument expiration_in_days", value=expiration_in_days, expected_type=type_hints["expiration_in_days"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument object_size_greater_than", value=object_size_greater_than, expected_type=type_hints["object_size_greater_than"])
                check_type(argname="argument object_size_less_than", value=object_size_less_than, expected_type=type_hints["object_size_less_than"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "status": status,
            }
            if abort_incomplete_multipart_upload is not None:
                self._values["abort_incomplete_multipart_upload"] = abort_incomplete_multipart_upload
            if expiration_in_days is not None:
                self._values["expiration_in_days"] = expiration_in_days
            if id is not None:
                self._values["id"] = id
            if object_size_greater_than is not None:
                self._values["object_size_greater_than"] = object_size_greater_than
            if object_size_less_than is not None:
                self._values["object_size_less_than"] = object_size_less_than
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def status(self) -> builtins.str:
            '''If ``Enabled`` , the rule is currently being applied.

            If ``Disabled`` , the rule is not currently being applied.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-rule.html#cfn-s3express-directorybucket-rule-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def abort_incomplete_multipart_upload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDirectoryBucket.AbortIncompleteMultipartUploadProperty"]]:
            '''Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before permanently removing all parts of the upload.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-rule.html#cfn-s3express-directorybucket-rule-abortincompletemultipartupload
            '''
            result = self._values.get("abort_incomplete_multipart_upload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDirectoryBucket.AbortIncompleteMultipartUploadProperty"]], result)

        @builtins.property
        def expiration_in_days(self) -> typing.Optional[jsii.Number]:
            '''Indicates the number of days after creation when objects are deleted from Amazon S3 and Amazon S3 Glacier.

            If you specify an expiration and transition time, you must use the same time unit for both properties (either in days or by date). The expiration time must also be later than the transition time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-rule.html#cfn-s3express-directorybucket-rule-expirationindays
            '''
            result = self._values.get("expiration_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''Unique identifier for the rule.

            The value can't be longer than 255 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-rule.html#cfn-s3express-directorybucket-rule-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_size_greater_than(self) -> typing.Optional[builtins.str]:
            '''Specifies the minimum object size in bytes for this rule to apply to.

            Objects must be larger than this value in bytes. For more information about size based rules, see `Lifecycle configuration using size-based rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html#lc-size-rules>`_ in the *Amazon S3 User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-rule.html#cfn-s3express-directorybucket-rule-objectsizegreaterthan
            '''
            result = self._values.get("object_size_greater_than")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_size_less_than(self) -> typing.Optional[builtins.str]:
            '''Specifies the maximum object size in bytes for this rule to apply to.

            Objects must be smaller than this value in bytes. For more information about sized based rules, see `Lifecycle configuration using size-based rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html#lc-size-rules>`_ in the *Amazon S3 User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-rule.html#cfn-s3express-directorybucket-rule-objectsizelessthan
            '''
            result = self._values.get("object_size_less_than")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''Object key prefix that identifies one or more objects to which this rule applies.

            .. epigraph::

               Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see `XML related object key constraints <https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-rule.html#cfn-s3express-directorybucket-rule-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3express.CfnDirectoryBucket.ServerSideEncryptionByDefaultProperty",
        jsii_struct_bases=[],
        name_mapping={
            "sse_algorithm": "sseAlgorithm",
            "kms_master_key_id": "kmsMasterKeyId",
        },
    )
    class ServerSideEncryptionByDefaultProperty:
        def __init__(
            self,
            *,
            sse_algorithm: builtins.str,
            kms_master_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the default server-side encryption to apply to new objects in the bucket.

            If a PUT Object request doesn't specify any server-side encryption, this default encryption will be applied. For more information, see `PutBucketEncryption <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTencryption.html>`_ in the *Amazon S3 API Reference* .

            :param sse_algorithm: Server-side encryption algorithm to use for the default encryption. .. epigraph:: For directory buckets, there are only two supported values for server-side encryption: ``AES256`` and ``aws:kms`` .
            :param kms_master_key_id: AWS Key Management Service (KMS) customer managed key ID to use for the default encryption. This parameter is allowed only if ``SSEAlgorithm`` is set to ``aws:kms`` . You can specify this parameter with the key ID or the Amazon Resource Name (ARN) of the KMS key. You can’t use the key alias of the KMS key. - Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab`` - Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` If you are using encryption with cross-account or AWS service operations, you must use a fully qualified KMS key ARN. For more information, see `Using encryption for cross-account operations <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-bucket-encryption.html#s3-express-bucket-encryption-update-bucket-policy>`_ . .. epigraph:: Your SSE-KMS configuration can only support 1 `customer managed key <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk>`_ per directory bucket for the lifetime of the bucket. `AWS managed key <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk>`_ ( ``aws/s3`` ) isn't supported. Also, after you specify a customer managed key for SSE-KMS and upload objects with this configuration, you can't override the customer managed key for your SSE-KMS configuration. To use a new customer manager key for your data, we recommend copying your existing objects to a new directory bucket with a new customer managed key. > Amazon S3 only supports symmetric encryption KMS keys. For more information, see `Asymmetric keys in AWS KMS <https://docs.aws.amazon.com//kms/latest/developerguide/symmetric-asymmetric.html>`_ in the *AWS Key Management Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-serversideencryptionbydefault.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3express as s3express
                
                server_side_encryption_by_default_property = s3express.CfnDirectoryBucket.ServerSideEncryptionByDefaultProperty(
                    sse_algorithm="sseAlgorithm",
                
                    # the properties below are optional
                    kms_master_key_id="kmsMasterKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5104b7dd2a8f7d075aebe34991fe63f5722d4515b7d5df7eadca88aa065daee9)
                check_type(argname="argument sse_algorithm", value=sse_algorithm, expected_type=type_hints["sse_algorithm"])
                check_type(argname="argument kms_master_key_id", value=kms_master_key_id, expected_type=type_hints["kms_master_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "sse_algorithm": sse_algorithm,
            }
            if kms_master_key_id is not None:
                self._values["kms_master_key_id"] = kms_master_key_id

        @builtins.property
        def sse_algorithm(self) -> builtins.str:
            '''Server-side encryption algorithm to use for the default encryption.

            .. epigraph::

               For directory buckets, there are only two supported values for server-side encryption: ``AES256`` and ``aws:kms`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-serversideencryptionbydefault.html#cfn-s3express-directorybucket-serversideencryptionbydefault-ssealgorithm
            '''
            result = self._values.get("sse_algorithm")
            assert result is not None, "Required property 'sse_algorithm' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_master_key_id(self) -> typing.Optional[builtins.str]:
            '''AWS Key Management Service (KMS) customer managed key ID to use for the default encryption.

            This parameter is allowed only if ``SSEAlgorithm`` is set to ``aws:kms`` .

            You can specify this parameter with the key ID or the Amazon Resource Name (ARN) of the KMS key. You can’t use the key alias of the KMS key.

            - Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``
            - Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

            If you are using encryption with cross-account or AWS service operations, you must use a fully qualified KMS key ARN. For more information, see `Using encryption for cross-account operations <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-bucket-encryption.html#s3-express-bucket-encryption-update-bucket-policy>`_ .
            .. epigraph::

               Your SSE-KMS configuration can only support 1 `customer managed key <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk>`_ per directory bucket for the lifetime of the bucket. `AWS managed key <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk>`_ ( ``aws/s3`` ) isn't supported. Also, after you specify a customer managed key for SSE-KMS and upload objects with this configuration, you can't override the customer managed key for your SSE-KMS configuration. To use a new customer manager key for your data, we recommend copying your existing objects to a new directory bucket with a new customer managed key. > Amazon S3 only supports symmetric encryption KMS keys. For more information, see `Asymmetric keys in AWS KMS <https://docs.aws.amazon.com//kms/latest/developerguide/symmetric-asymmetric.html>`_ in the *AWS Key Management Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-serversideencryptionbydefault.html#cfn-s3express-directorybucket-serversideencryptionbydefault-kmsmasterkeyid
            '''
            result = self._values.get("kms_master_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerSideEncryptionByDefaultProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3express.CfnDirectoryBucket.ServerSideEncryptionRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_key_enabled": "bucketKeyEnabled",
            "server_side_encryption_by_default": "serverSideEncryptionByDefault",
        },
    )
    class ServerSideEncryptionRuleProperty:
        def __init__(
            self,
            *,
            bucket_key_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            server_side_encryption_by_default: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDirectoryBucket.ServerSideEncryptionByDefaultProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the default server-side encryption configuration.

            :param bucket_key_enabled: Specifies whether Amazon S3 should use an S3 Bucket Key with server-side encryption using KMS (SSE-KMS) for new objects in the bucket. S3 Bucket Keys are always enabled for ``GET`` and ``PUT`` operations on a directory bucket and can’t be disabled. It's only allowed to set the ``BucketKeyEnabled`` element to ``true`` . S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through `CopyObject <https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html>`_ , `UploadPartCopy <https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html>`_ , `the Copy operation in Batch Operations <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops>`_ , or `the import jobs <https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job>`_ . In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object. For more information, see `Amazon S3 Bucket Keys <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-UsingKMSEncryption.html#s3-express-sse-kms-bucket-keys>`_ in the *Amazon S3 User Guide* .
            :param server_side_encryption_by_default: Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT Object request doesn't specify any server-side encryption, this default encryption will be applied.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-serversideencryptionrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3express as s3express
                
                server_side_encryption_rule_property = s3express.CfnDirectoryBucket.ServerSideEncryptionRuleProperty(
                    bucket_key_enabled=False,
                    server_side_encryption_by_default=s3express.CfnDirectoryBucket.ServerSideEncryptionByDefaultProperty(
                        sse_algorithm="sseAlgorithm",
                
                        # the properties below are optional
                        kms_master_key_id="kmsMasterKeyId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb4bc307ba12040c7d9910685d8ea50fd2f9f3f34fdecd3ca61c34ccd69e3dbf)
                check_type(argname="argument bucket_key_enabled", value=bucket_key_enabled, expected_type=type_hints["bucket_key_enabled"])
                check_type(argname="argument server_side_encryption_by_default", value=server_side_encryption_by_default, expected_type=type_hints["server_side_encryption_by_default"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_key_enabled is not None:
                self._values["bucket_key_enabled"] = bucket_key_enabled
            if server_side_encryption_by_default is not None:
                self._values["server_side_encryption_by_default"] = server_side_encryption_by_default

        @builtins.property
        def bucket_key_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether Amazon S3 should use an S3 Bucket Key with server-side encryption using KMS (SSE-KMS) for new objects in the bucket.

            S3 Bucket Keys are always enabled for ``GET`` and ``PUT`` operations on a directory bucket and can’t be disabled. It's only allowed to set the ``BucketKeyEnabled`` element to ``true`` .

            S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through `CopyObject <https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html>`_ , `UploadPartCopy <https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html>`_ , `the Copy operation in Batch Operations <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops>`_ , or `the import jobs <https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job>`_ . In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object.

            For more information, see `Amazon S3 Bucket Keys <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-UsingKMSEncryption.html#s3-express-sse-kms-bucket-keys>`_ in the *Amazon S3 User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-serversideencryptionrule.html#cfn-s3express-directorybucket-serversideencryptionrule-bucketkeyenabled
            '''
            result = self._values.get("bucket_key_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def server_side_encryption_by_default(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDirectoryBucket.ServerSideEncryptionByDefaultProperty"]]:
            '''Specifies the default server-side encryption to apply to new objects in the bucket.

            If a PUT Object request doesn't specify any server-side encryption, this default encryption will be applied.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3express-directorybucket-serversideencryptionrule.html#cfn-s3express-directorybucket-serversideencryptionrule-serversideencryptionbydefault
            '''
            result = self._values.get("server_side_encryption_by_default")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDirectoryBucket.ServerSideEncryptionByDefaultProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerSideEncryptionRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3express.CfnDirectoryBucketProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_redundancy": "dataRedundancy",
        "location_name": "locationName",
        "bucket_encryption": "bucketEncryption",
        "bucket_name": "bucketName",
        "lifecycle_configuration": "lifecycleConfiguration",
    },
)
class CfnDirectoryBucketProps:
    def __init__(
        self,
        *,
        data_redundancy: builtins.str,
        location_name: builtins.str,
        bucket_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryBucket.BucketEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryBucket.LifecycleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDirectoryBucket``.

        :param data_redundancy: The number of Zone (Availability Zone or Local Zone) that's used for redundancy for the bucket.
        :param location_name: The name of the location where the bucket will be created. For directory buckets, the name of the location is the Zone ID of the Availability Zone (AZ) or Local Zone (LZ) where the bucket will be created. An example AZ ID value is ``usw2-az1`` .
        :param bucket_encryption: Specifies default encryption for a bucket using server-side encryption with Amazon S3 managed keys (SSE-S3) or AWS KMS keys (SSE-KMS). For information about default encryption for directory buckets, see `Setting and monitoring default encryption for directory buckets <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-bucket-encryption.html>`_ in the *Amazon S3 User Guide* .
        :param bucket_name: A name for the bucket. The bucket name must contain only lowercase letters, numbers, and hyphens (-). A directory bucket name must be unique in the chosen Zone (Availability Zone or Local Zone). The bucket name must also follow the format ``*bucket_base_name* -- *zone_id* --x-s3`` (for example, ``*bucket_base_name* -- *usw2-az1* --x-s3`` ). If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. For information about bucket naming restrictions, see `Directory bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html>`_ in the *Amazon S3 User Guide* . .. epigraph:: If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.
        :param lifecycle_configuration: Container for lifecycle rules. You can add as many as 1000 rules. For more information see, `Creating and managing a lifecycle configuration for directory buckets <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-lifecycle.html>`_ in the *Amazon S3 User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3express as s3express
            
            cfn_directory_bucket_props = s3express.CfnDirectoryBucketProps(
                data_redundancy="dataRedundancy",
                location_name="locationName",
            
                # the properties below are optional
                bucket_encryption=s3express.CfnDirectoryBucket.BucketEncryptionProperty(
                    server_side_encryption_configuration=[s3express.CfnDirectoryBucket.ServerSideEncryptionRuleProperty(
                        bucket_key_enabled=False,
                        server_side_encryption_by_default=s3express.CfnDirectoryBucket.ServerSideEncryptionByDefaultProperty(
                            sse_algorithm="sseAlgorithm",
            
                            # the properties below are optional
                            kms_master_key_id="kmsMasterKeyId"
                        )
                    )]
                ),
                bucket_name="bucketName",
                lifecycle_configuration=s3express.CfnDirectoryBucket.LifecycleConfigurationProperty(
                    rules=[s3express.CfnDirectoryBucket.RuleProperty(
                        status="status",
            
                        # the properties below are optional
                        abort_incomplete_multipart_upload=s3express.CfnDirectoryBucket.AbortIncompleteMultipartUploadProperty(
                            days_after_initiation=123
                        ),
                        expiration_in_days=123,
                        id="id",
                        object_size_greater_than="objectSizeGreaterThan",
                        object_size_less_than="objectSizeLessThan",
                        prefix="prefix"
                    )]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__997b2abc28c849393aef2f13f43682b271277998e07114f1b224078949985e6e)
            check_type(argname="argument data_redundancy", value=data_redundancy, expected_type=type_hints["data_redundancy"])
            check_type(argname="argument location_name", value=location_name, expected_type=type_hints["location_name"])
            check_type(argname="argument bucket_encryption", value=bucket_encryption, expected_type=type_hints["bucket_encryption"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument lifecycle_configuration", value=lifecycle_configuration, expected_type=type_hints["lifecycle_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_redundancy": data_redundancy,
            "location_name": location_name,
        }
        if bucket_encryption is not None:
            self._values["bucket_encryption"] = bucket_encryption
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if lifecycle_configuration is not None:
            self._values["lifecycle_configuration"] = lifecycle_configuration

    @builtins.property
    def data_redundancy(self) -> builtins.str:
        '''The number of Zone (Availability Zone or Local Zone) that's used for redundancy for the bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html#cfn-s3express-directorybucket-dataredundancy
        '''
        result = self._values.get("data_redundancy")
        assert result is not None, "Required property 'data_redundancy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location_name(self) -> builtins.str:
        '''The name of the location where the bucket will be created.

        For directory buckets, the name of the location is the Zone ID of the Availability Zone (AZ) or Local Zone (LZ) where the bucket will be created. An example AZ ID value is ``usw2-az1`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html#cfn-s3express-directorybucket-locationname
        '''
        result = self._values.get("location_name")
        assert result is not None, "Required property 'location_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_encryption(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDirectoryBucket.BucketEncryptionProperty]]:
        '''Specifies default encryption for a bucket using server-side encryption with Amazon S3 managed keys (SSE-S3) or AWS KMS keys (SSE-KMS).

        For information about default encryption for directory buckets, see `Setting and monitoring default encryption for directory buckets <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-bucket-encryption.html>`_ in the *Amazon S3 User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html#cfn-s3express-directorybucket-bucketencryption
        '''
        result = self._values.get("bucket_encryption")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDirectoryBucket.BucketEncryptionProperty]], result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''A name for the bucket.

        The bucket name must contain only lowercase letters, numbers, and hyphens (-). A directory bucket name must be unique in the chosen Zone (Availability Zone or Local Zone). The bucket name must also follow the format ``*bucket_base_name* -- *zone_id* --x-s3`` (for example, ``*bucket_base_name* -- *usw2-az1* --x-s3`` ). If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. For information about bucket naming restrictions, see `Directory bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html>`_ in the *Amazon S3 User Guide* .
        .. epigraph::

           If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html#cfn-s3express-directorybucket-bucketname
        '''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDirectoryBucket.LifecycleConfigurationProperty]]:
        '''Container for lifecycle rules. You can add as many as 1000 rules.

        For more information see, `Creating and managing a lifecycle configuration for directory buckets <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-lifecycle.html>`_ in the *Amazon S3 User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html#cfn-s3express-directorybucket-lifecycleconfiguration
        '''
        result = self._values.get("lifecycle_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDirectoryBucket.LifecycleConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDirectoryBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBucketPolicy",
    "CfnBucketPolicyProps",
    "CfnDirectoryBucket",
    "CfnDirectoryBucketProps",
]

publication.publish()

def _typecheckingstub__c7ae0c19fbf2c7c716bc3304458f2695912d196d3e7439999f721b69fdbfc5a0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bucket: builtins.str,
    policy_document: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0da69b8aee8ed367e63ca61c9ad9c6ce2b5fd2aff3c02cb553118847c89867c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a427439734058e5e6251cd5c0aaeed7ade47e92954992912236d939d3b496350(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dedf6ffab37d96f5ca0d97fbcb6904b8dc185fd26912baba5f2b683aec30a5e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__575ca46990b1014411a210bab87827014d15a4bd9119ec2a06a134d0e642cfff(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7978963298afc97ec8564e6e114bf73c7797f21fb71f9d0a187dd5852499f423(
    *,
    bucket: builtins.str,
    policy_document: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea5a1e5897b0467fb93393ad6ea2dbcd3916f27713079e8bef3badf71ce2bb20(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_redundancy: builtins.str,
    location_name: builtins.str,
    bucket_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryBucket.BucketEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    bucket_name: typing.Optional[builtins.str] = None,
    lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryBucket.LifecycleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61d4c01a14f34a0546048356b166c111adde5de129e3d0580f9ce73d26da1587(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09d4f293955716375e6177306d2bdfa8106614896e901a12247190cc871e9e61(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9234d8f5c9448b0bb44f48a13430731436331b4ef073722b1511600f9484ff5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__352b4b43cbbf4d81310eac7a66fd236d34a92a5af6e8099d48e6ec1e7c90c7a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec12f12e4471077fcc9afe2e16208df6b915dc349584d6784410dc28aeaa9ac3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDirectoryBucket.BucketEncryptionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__678dc679eb1daf10bbced208f7ef85b8fe01f1ae8ea62c5354ac80b289edc1ed(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddfd3872142b33ae9fa409c0018df1c791508213de3582b65e63e55af438eb3b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDirectoryBucket.LifecycleConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94d67335bbcb78d0b027e59764707d68d59cd3646befac6651614e419d8af6f4(
    *,
    days_after_initiation: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bda13f500a0910d95ef795cf250698cc9bc399a6809500b0318dd2399fa0dfc(
    *,
    server_side_encryption_configuration: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryBucket.ServerSideEncryptionRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82d5e100390b1400bc989c8f7007f04e65bff5948bb5f68def580a8385603442(
    *,
    rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryBucket.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6f9e06e8b8beb4ef85714d8e61855121cd4a13b083bc1c2de944bad75acf266(
    *,
    status: builtins.str,
    abort_incomplete_multipart_upload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryBucket.AbortIncompleteMultipartUploadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    expiration_in_days: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    object_size_greater_than: typing.Optional[builtins.str] = None,
    object_size_less_than: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5104b7dd2a8f7d075aebe34991fe63f5722d4515b7d5df7eadca88aa065daee9(
    *,
    sse_algorithm: builtins.str,
    kms_master_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb4bc307ba12040c7d9910685d8ea50fd2f9f3f34fdecd3ca61c34ccd69e3dbf(
    *,
    bucket_key_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    server_side_encryption_by_default: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryBucket.ServerSideEncryptionByDefaultProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__997b2abc28c849393aef2f13f43682b271277998e07114f1b224078949985e6e(
    *,
    data_redundancy: builtins.str,
    location_name: builtins.str,
    bucket_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryBucket.BucketEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    bucket_name: typing.Optional[builtins.str] = None,
    lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDirectoryBucket.LifecycleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
