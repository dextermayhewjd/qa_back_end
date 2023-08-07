# Full Stack Back-end Deployment

This repository contains the Dockerfile and GitHub Actions configuration files for deploying the full stack back-end application to AWS Elastic Beanstalk. The back-end application is built using Django and is deployed using Docker containers.

## Dockerfile

The `Dockerfile` in this repository is used to create the Docker image for the Django back-end application. It uses the `continuumio/miniconda3:latest` base image and sets up the necessary environment for the application.

### Build Stage

In the build stage, the necessary dependencies are installed using Conda and Pip. The `environment2.yml` file is copied to the container and the Conda environment is created based on this file. Pip dependencies are installed using the requirements specified in `myapp/requirements.txt`.

### Run Stage

In the run stage, the previously installed dependencies and the project files are copied from the build stage. The environment variable `DJANGO_SETTINGS_MODULE` is set to `first_project.settings` to configure Django settings. The application is set to listen on port 8000.

## GitHub Actions

The repository is configured with GitHub Actions to automate the deployment process to AWS Elastic Beanstalk.

### `build-and-push-docker-image` Workflow

This workflow is triggered on each push to the specified branches. It builds the Docker image, tags it with the GitHub commit SHA, and pushes it to the Docker registry (Docker Hub).

### `prepare-and-upload-dockerrun-file` Workflow

This workflow is triggered after successfully building and pushing the Docker image. It prepares the `Dockerrun.aws.json` file, which is used by AWS Elastic Beanstalk to deploy the application. The file specifies the Docker image to be used and the port on which the application will listen.

The `Dockerrun.aws.json` file is zipped and uploaded to an S3 bucket on AWS.

The steps for this workflow are as follows:

1. Prepare the `Dockerrun.aws.json` file using a `run` command, which creates the necessary configuration for AWS Elastic Beanstalk.

2. Zip the `Dockerrun.aws.json` file into `myapp.zip` using the `run` command with `zip`.

3. Configure AWS credentials using `aws-actions/configure-aws-credentials@v1` with the AWS access key ID and secret access key from GitHub secrets.

4. Upload `myapp.zip` to an S3 bucket on AWS using the `aws s3 cp` command.

### `deploy-to-elastic-beanstalk` Workflow

This workflow is triggered after the `prepare-and-upload-dockerrun-file` workflow completes successfully. It deploys the application to AWS Elastic Beanstalk.

It creates a new application version with a label generated based on the GitHub commit SHA. The application version is updated in the Elastic Beanstalk environment, triggering a deployment of the new version.

Please ensure that you have configured the necessary GitHub secrets and AWS credentials for the workflows to run successfully.

The steps for this workflow are as follows:

1. Generate a version label using a `run` command and save it to the GitHub environment variable.

2. Create a new application version on Elastic Beanstalk using `aws elasticbeanstalk create-application-version` with the version label and the S3 bucket and key for the source bundle.

3. Update the Elastic Beanstalk environment to use the new application version using `aws elasticbeanstalk update-environment` with the application name, environment name, and version label.


## GitHub Secrets

Make sure to set the following GitHub secrets in your repository:

- `DOCKERHUB_USERNAME`: Your Docker Hub username for pushing the Docker image.
- `DOCKERHUB_PASSWORD`: Your Docker Hub password for pushing the Docker image.
- `AWS_ACCESS_KEY_ID`: Your AWS access key ID for deploying to Elastic Beanstalk.
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key for deploying to Elastic Beanstalk.

