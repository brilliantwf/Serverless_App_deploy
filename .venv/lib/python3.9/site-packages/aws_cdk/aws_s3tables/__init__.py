r'''
# AWS::S3Tables Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_s3tables as s3tables
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for S3Tables construct libraries](https://constructs.dev/search?q=s3tables)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::S3Tables resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Tables.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::S3Tables](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Tables.html).

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
class CfnTableBucket(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3tables.CfnTableBucket",
):
    '''Creates a table bucket.

    For more information, see `Creating a table bucket <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-create.html>`_ in the *Amazon Simple Storage Service User Guide* .

    - **Permissions** - You must have the ``s3tables:CreateTableBucket`` permission to use this operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucket.html
    :cloudformationResource: AWS::S3Tables::TableBucket
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3tables as s3tables
        
        cfn_table_bucket = s3tables.CfnTableBucket(self, "MyCfnTableBucket",
            table_bucket_name="tableBucketName",
        
            # the properties below are optional
            unreferenced_file_removal=s3tables.CfnTableBucket.UnreferencedFileRemovalProperty(
                noncurrent_days=123,
                status="status",
                unreferenced_days=123
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        table_bucket_name: builtins.str,
        unreferenced_file_removal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTableBucket.UnreferencedFileRemovalProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param table_bucket_name: The name for the table bucket.
        :param unreferenced_file_removal: The unreferenced file removal settings for your table bucket. Unreferenced file removal identifies and deletes all objects that are not referenced by any table snapshots. For more information, see the `*Amazon S3 User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de433918cd34eecbcaab0e81b6a287f71a48dd308c2f4d42e07a0e19ce5af0e2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTableBucketProps(
            table_bucket_name=table_bucket_name,
            unreferenced_file_removal=unreferenced_file_removal,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40da426af74874eef485654394ab5db25ba5f82e8490b96bd68d9f6318b6654e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e15cdb1ab81b354e389c0debd6b2b9d760245945e38c20d735044cde53c3979)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrTableBucketArn")
    def attr_table_bucket_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the table bucket.

        :cloudformationAttribute: TableBucketARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTableBucketArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tableBucketName")
    def table_bucket_name(self) -> builtins.str:
        '''The name for the table bucket.'''
        return typing.cast(builtins.str, jsii.get(self, "tableBucketName"))

    @table_bucket_name.setter
    def table_bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42ef5079e6a92822a2e6ccbb91b02661f493a7d44dc79dfba0916840dbe44863)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableBucketName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="unreferencedFileRemoval")
    def unreferenced_file_removal(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTableBucket.UnreferencedFileRemovalProperty"]]:
        '''The unreferenced file removal settings for your table bucket.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTableBucket.UnreferencedFileRemovalProperty"]], jsii.get(self, "unreferencedFileRemoval"))

    @unreferenced_file_removal.setter
    def unreferenced_file_removal(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTableBucket.UnreferencedFileRemovalProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02bf42691243dcbc8ea49c2499d3414260e70a80c4e38a371b64664c49f17e6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unreferencedFileRemoval", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3tables.CfnTableBucket.UnreferencedFileRemovalProperty",
        jsii_struct_bases=[],
        name_mapping={
            "noncurrent_days": "noncurrentDays",
            "status": "status",
            "unreferenced_days": "unreferencedDays",
        },
    )
    class UnreferencedFileRemovalProperty:
        def __init__(
            self,
            *,
            noncurrent_days: typing.Optional[jsii.Number] = None,
            status: typing.Optional[builtins.str] = None,
            unreferenced_days: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The unreferenced file removal settings for your table bucket.

            Unreferenced file removal identifies and deletes all objects that are not referenced by any table snapshots. For more information, see the `*Amazon S3 User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html>`_ .

            :param noncurrent_days: The number of days an object can be noncurrent before Amazon S3 deletes it.
            :param status: The status of the unreferenced file removal configuration for your table bucket.
            :param unreferenced_days: The number of days an object must be unreferenced by your table before Amazon S3 marks the object as noncurrent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-tablebucket-unreferencedfileremoval.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3tables as s3tables
                
                unreferenced_file_removal_property = s3tables.CfnTableBucket.UnreferencedFileRemovalProperty(
                    noncurrent_days=123,
                    status="status",
                    unreferenced_days=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e5a5e0b11a3cbe8be01a72f3ac6efc85af9472104c94585d26f630d3354c816b)
                check_type(argname="argument noncurrent_days", value=noncurrent_days, expected_type=type_hints["noncurrent_days"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument unreferenced_days", value=unreferenced_days, expected_type=type_hints["unreferenced_days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if noncurrent_days is not None:
                self._values["noncurrent_days"] = noncurrent_days
            if status is not None:
                self._values["status"] = status
            if unreferenced_days is not None:
                self._values["unreferenced_days"] = unreferenced_days

        @builtins.property
        def noncurrent_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days an object can be noncurrent before Amazon S3 deletes it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-tablebucket-unreferencedfileremoval.html#cfn-s3tables-tablebucket-unreferencedfileremoval-noncurrentdays
            '''
            result = self._values.get("noncurrent_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the unreferenced file removal configuration for your table bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-tablebucket-unreferencedfileremoval.html#cfn-s3tables-tablebucket-unreferencedfileremoval-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unreferenced_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days an object must be unreferenced by your table before Amazon S3 marks the object as noncurrent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-tablebucket-unreferencedfileremoval.html#cfn-s3tables-tablebucket-unreferencedfileremoval-unreferenceddays
            '''
            result = self._values.get("unreferenced_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UnreferencedFileRemovalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnTableBucketPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3tables.CfnTableBucketPolicy",
):
    '''Creates a new maintenance configuration or replaces an existing table bucket policy for a table bucket.

    For more information, see `Adding a table bucket policy <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-add>`_ in the *Amazon Simple Storage Service User Guide* .

    - **Permissions** - You must have the ``s3tables:PutTableBucketPolicy`` permission to use this operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucketpolicy.html
    :cloudformationResource: AWS::S3Tables::TableBucketPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3tables as s3tables
        
        # resource_policy: Any
        
        cfn_table_bucket_policy = s3tables.CfnTableBucketPolicy(self, "MyCfnTableBucketPolicy",
            resource_policy=resource_policy,
            table_bucket_arn="tableBucketArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resource_policy: typing.Any,
        table_bucket_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resource_policy: The bucket policy JSON for the table bucket.
        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e41d1f33249c074a27c8db71a0d74f7ec78216836901a699d5ff7dbdcfdcf89a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTableBucketPolicyProps(
            resource_policy=resource_policy, table_bucket_arn=table_bucket_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a8346fde6b51dff587833e7cd68ccdd12e4f80b4b07e756c507ac9d8b81cfdb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__32d2b3e7f152d93640c11f17b345fb2a9bf95efe6dd3c1235a1d9ca148caae1a)
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
    @jsii.member(jsii_name="resourcePolicy")
    def resource_policy(self) -> typing.Any:
        '''The bucket policy JSON for the table bucket.'''
        return typing.cast(typing.Any, jsii.get(self, "resourcePolicy"))

    @resource_policy.setter
    def resource_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60d686568fe0e9bc1be86d3585b33d6e6dcf5d8ec00b2b4b4ba9c5e48ea4cd82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcePolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tableBucketArn")
    def table_bucket_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the table bucket.'''
        return typing.cast(builtins.str, jsii.get(self, "tableBucketArn"))

    @table_bucket_arn.setter
    def table_bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9db770e8febae7602179359c1a5975b5ae8be6270348474fc3a1cca79c47ad2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableBucketArn", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3tables.CfnTableBucketPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "resource_policy": "resourcePolicy",
        "table_bucket_arn": "tableBucketArn",
    },
)
class CfnTableBucketPolicyProps:
    def __init__(
        self,
        *,
        resource_policy: typing.Any,
        table_bucket_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnTableBucketPolicy``.

        :param resource_policy: The bucket policy JSON for the table bucket.
        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucketpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3tables as s3tables
            
            # resource_policy: Any
            
            cfn_table_bucket_policy_props = s3tables.CfnTableBucketPolicyProps(
                resource_policy=resource_policy,
                table_bucket_arn="tableBucketArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df8972559ed3d0ff90d01d70d1cf8f77869398b91f03a408d49a7b5bee0615a0)
            check_type(argname="argument resource_policy", value=resource_policy, expected_type=type_hints["resource_policy"])
            check_type(argname="argument table_bucket_arn", value=table_bucket_arn, expected_type=type_hints["table_bucket_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_policy": resource_policy,
            "table_bucket_arn": table_bucket_arn,
        }

    @builtins.property
    def resource_policy(self) -> typing.Any:
        '''The bucket policy JSON for the table bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucketpolicy.html#cfn-s3tables-tablebucketpolicy-resourcepolicy
        '''
        result = self._values.get("resource_policy")
        assert result is not None, "Required property 'resource_policy' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def table_bucket_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the table bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucketpolicy.html#cfn-s3tables-tablebucketpolicy-tablebucketarn
        '''
        result = self._values.get("table_bucket_arn")
        assert result is not None, "Required property 'table_bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTableBucketPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3tables.CfnTableBucketProps",
    jsii_struct_bases=[],
    name_mapping={
        "table_bucket_name": "tableBucketName",
        "unreferenced_file_removal": "unreferencedFileRemoval",
    },
)
class CfnTableBucketProps:
    def __init__(
        self,
        *,
        table_bucket_name: builtins.str,
        unreferenced_file_removal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTableBucket.UnreferencedFileRemovalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTableBucket``.

        :param table_bucket_name: The name for the table bucket.
        :param unreferenced_file_removal: The unreferenced file removal settings for your table bucket. Unreferenced file removal identifies and deletes all objects that are not referenced by any table snapshots. For more information, see the `*Amazon S3 User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucket.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3tables as s3tables
            
            cfn_table_bucket_props = s3tables.CfnTableBucketProps(
                table_bucket_name="tableBucketName",
            
                # the properties below are optional
                unreferenced_file_removal=s3tables.CfnTableBucket.UnreferencedFileRemovalProperty(
                    noncurrent_days=123,
                    status="status",
                    unreferenced_days=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fb9342a13c0e9f7b21679814e793d7ccc0964ccfe53bc5e0916676b628d20f3)
            check_type(argname="argument table_bucket_name", value=table_bucket_name, expected_type=type_hints["table_bucket_name"])
            check_type(argname="argument unreferenced_file_removal", value=unreferenced_file_removal, expected_type=type_hints["unreferenced_file_removal"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table_bucket_name": table_bucket_name,
        }
        if unreferenced_file_removal is not None:
            self._values["unreferenced_file_removal"] = unreferenced_file_removal

    @builtins.property
    def table_bucket_name(self) -> builtins.str:
        '''The name for the table bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucket.html#cfn-s3tables-tablebucket-tablebucketname
        '''
        result = self._values.get("table_bucket_name")
        assert result is not None, "Required property 'table_bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def unreferenced_file_removal(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTableBucket.UnreferencedFileRemovalProperty]]:
        '''The unreferenced file removal settings for your table bucket.

        Unreferenced file removal identifies and deletes all objects that are not referenced by any table snapshots. For more information, see the `*Amazon S3 User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucket.html#cfn-s3tables-tablebucket-unreferencedfileremoval
        '''
        result = self._values.get("unreferenced_file_removal")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTableBucket.UnreferencedFileRemovalProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTableBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnTableBucket",
    "CfnTableBucketPolicy",
    "CfnTableBucketPolicyProps",
    "CfnTableBucketProps",
]

publication.publish()

def _typecheckingstub__de433918cd34eecbcaab0e81b6a287f71a48dd308c2f4d42e07a0e19ce5af0e2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    table_bucket_name: builtins.str,
    unreferenced_file_removal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTableBucket.UnreferencedFileRemovalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40da426af74874eef485654394ab5db25ba5f82e8490b96bd68d9f6318b6654e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e15cdb1ab81b354e389c0debd6b2b9d760245945e38c20d735044cde53c3979(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42ef5079e6a92822a2e6ccbb91b02661f493a7d44dc79dfba0916840dbe44863(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02bf42691243dcbc8ea49c2499d3414260e70a80c4e38a371b64664c49f17e6e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTableBucket.UnreferencedFileRemovalProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5a5e0b11a3cbe8be01a72f3ac6efc85af9472104c94585d26f630d3354c816b(
    *,
    noncurrent_days: typing.Optional[jsii.Number] = None,
    status: typing.Optional[builtins.str] = None,
    unreferenced_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e41d1f33249c074a27c8db71a0d74f7ec78216836901a699d5ff7dbdcfdcf89a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resource_policy: typing.Any,
    table_bucket_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a8346fde6b51dff587833e7cd68ccdd12e4f80b4b07e756c507ac9d8b81cfdb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32d2b3e7f152d93640c11f17b345fb2a9bf95efe6dd3c1235a1d9ca148caae1a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60d686568fe0e9bc1be86d3585b33d6e6dcf5d8ec00b2b4b4ba9c5e48ea4cd82(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9db770e8febae7602179359c1a5975b5ae8be6270348474fc3a1cca79c47ad2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df8972559ed3d0ff90d01d70d1cf8f77869398b91f03a408d49a7b5bee0615a0(
    *,
    resource_policy: typing.Any,
    table_bucket_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fb9342a13c0e9f7b21679814e793d7ccc0964ccfe53bc5e0916676b628d20f3(
    *,
    table_bucket_name: builtins.str,
    unreferenced_file_removal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTableBucket.UnreferencedFileRemovalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
