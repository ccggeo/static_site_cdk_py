#!/usr/bin/env python3

from aws_cdk import core

from personal_site.personal_site_stack import PersonalSiteStack
from personal_site.certs_stack import CertsStack
from personal_site.pipeline_stack import PipelineStack


app = core.App()
certs_stack = CertsStack(app, "certs", env=core.Environment(account="ACCOUNT_NO", region="us-east-1"))
personal_site = PersonalSiteStack(app, "personal-site", env=core.Environment(account="ACCOUNT_NO", region="eu-west-2"))
PipelineStack(app, "pipeline", env=core.Environment(account="ACCOUNT_NO", region="eu-west-2"), repo_name="REPO_NAME", bucket=personal_site.bucket) 

app.synth()
