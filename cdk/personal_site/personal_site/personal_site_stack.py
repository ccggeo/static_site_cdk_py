from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_cloudfront as cf,
    custom_resources as cr,
    aws_codebuild as codebuild,
    aws_codecommit as codecommit,
    aws_codepipeline as codepipeline,
    aws_secretsmanager as sm,
    aws_codepipeline_actions as codepipeline_actions
    )

import time
import stack_vars

class PersonalSiteStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
 
        self.bucket = s3.Bucket(self, "bucket",
                           website_index_document=f"{stack_vars.root_html}",
                           bucket_name=f"{stack_vars.bucket_name}"
                           )
        self.bucket.grant_public_access()
        names=[f"{stack_vars.bucket_name}", f"www.{stack_vars.bucket_name}"],

        cf.CloudFrontWebDistribution(self, "cloudwebdistribution",
                                 price_class=cf.PriceClass.PRICE_CLASS_ALL,
                                 default_root_object=f"{stack_vars.root_html}",
                                 alias_configuration=cf.AliasConfiguration(
                                     ssl_method=cf.SSLMethod.SNI,
                                     acm_cert_ref=stack_vars.cert_arn,
                                     names=[f"{stack_vars.bucket_name}", f"www.{stack_vars.bucket_name}"],
                                     security_policy=cf.SecurityPolicyProtocol.TLS_V1_2_2018
                                 ),
                                 origin_configs=[
                                     cf.SourceConfiguration(
                                         behaviors=[
                                             cf.Behavior(
                                                 is_default_behavior=True)
                                         ],
                                         s3_origin_source=cf.S3OriginConfig(
                                             s3_bucket_source=self.bucket
                                         )
                                     )
                                 ]
                             )
