# CI/CD Pipeline for AWS Lambda

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI or via AWS CodePipeline.

## Project Structure

- `lambda_function.py` - Code for the application's Lambda function.
- `template.yaml` - A template that defines the application's AWS resources.
- `buildspec.yml` - The build specification for AWS CodeBuild.

## Deployment Instructions

### Prerequisites

1. An AWS Account.
2. IAM Role for CodeBuild with permissions to:
    - Create/Update CloudFormation stacks.
    - Create/Update Lambda functions.
    - Put objects to S3 (SAM will resolve an S3 bucket for artifacts).
    - Create IAM roles (if the stack creates new roles).

### Setup

1. **Push to Repository**: Push these files to your AWS CodeCommit repository or GitHub/Bitbucket repository.
2. **Create CodeBuild Project**:
    - Source: Your repository.
    - Buildspec: Use the `buildspec.yml` in the root.
    - Environment: Managed image (e.g., Ubuntu, Python 3.9).
    - Service Role: Ensure it has the necessary permissions (discussed above).
3. **Run Build**: Start the build in CodeBuild. It will execute `sam deploy` which creates the CloudFormation stack `my-cicd-lambda-stack`.

### Alternative: CodePipeline

For a full pipeline:
1. Create a Pipeline in AWS CodePipeline.
2. **Source Stage**: Connect to your repo.
3. **Build Stage**: Use CodeBuild with this `buildspec.yml`.
4. **Deploy Stage** (Optional if `sam deploy` is in buildspec): You can remove `sam deploy` from `buildspec.yml` and use the `CodePipeline` Deploy provider with CloudFormation, but the current setup does everything in the Build phase for simplicity as requested ("just deploy").
