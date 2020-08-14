#!/usr/bin/env python3

from aws_cdk import core

from personal_site.personal_site_stack import PersonalSiteStack
from personal_site.certs_stack import CertsStack


app = core.App()
certs_stack = CertsStack(app, "certs", env=core.Environment(region="us-east-1"))
PersonalSiteStack(app, "personal-site", env=core.Environment(region="eu-west-2")) 

app.synth()
