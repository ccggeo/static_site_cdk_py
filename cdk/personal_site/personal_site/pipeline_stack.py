from aws_cdk import (core, 
                     aws_codepipeline as codepipeline,
                     aws_codepipeline_actions as codepipeline_actions,
                     aws_secretsmanager as sm)

class PipelineStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, *, repo_name: str=None, bucket,
            **kwargs) -> None:

        super().__init__(scope, id, **kwargs)
        github_secret_personal_site = sm.Secret(self,  'github_secret_personal_site', description=f'{__name__} secret for github', \
                secret_name='github_secret_personal_site')

        personal_site_pipeline = codepipeline.Pipeline(self, "Pipeline", pipeline_name="personal_site_github"
            )

        source_output = codepipeline.Artifact()

        source_action = codepipeline_actions.GitHubSourceAction(
            action_name="GitHub_Source",
            owner=repo_name.split('/')[0],
            repo=repo_name.split('/')[1],
            oauth_token=core.SecretValue.secrets_manager("github_secret_personal_site"),
            output=source_output,
            branch="master"
        )

        deploy_action = codepipeline_actions.S3DeployAction(
            action_name="S3Deploy",
            bucket=bucket,
            input=source_output
        )

        #Add the stages defined above to the pipeline
        personal_site_pipeline.add_stage(
                stage_name="Source",
                actions=[source_action]
        )

        personal_site_pipeline.add_stage(
                stage_name="Deploy",
                actions=[deploy_action]
        )

