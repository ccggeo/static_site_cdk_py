from aws_cdk import (
    core,
    aws_ssm as ssm,
    aws_certificatemanager as cm,
)
import stack_vars
 
class CertsStack(core.Stack):
 
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
 
        certificate = cm.Certificate(self, "certs",
                                     domain_name=f"{stack_vars.bucket_name}"
                                     subject_alternative_names=[f"www.{stack_vars.bucket_name}"],
                                     validation_method=cm.ValidationMethod.DNS
                                     )
