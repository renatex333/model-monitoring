# Managing Machine Learning Workflows with MLflow

## Overview

As computer engineers, we recognize the significance of version control and Git flow in software development. These tools provide a systematic approach to managing code changes, enabling collaboration, version control, and seamless integration of new features. 

In machine learning (ML), the development process is slightly different. Instead of focusing solely on functional requirements, ML projects are centered around optimizing metrics such as accuracy or mean squared error (MSE). As a result, in addition to code quality, the quality of the data becomes critical in determining the success of the project.

Imagine you’ve developed an ML product and completed deployment. Scenarios may arise where updates are required, such as:
- Retraining the model on new data
- Adding new features to the model
- Developing new algorithms

During these updates, comparing metrics is essential to validate that the modifications improve the model's performance.

## MLflow: Managing Machine Learning Workflows

MLflow is an open-source platform designed to manage and organize ML workflows efficiently. It allows you to log parameters, metrics, and artifacts, providing an easy way to monitor and track ML experiments. By integrating MLflow into your projects, you can apply MLOps principles with minimal changes to your existing code.

### Key Concepts in MLflow:

- **Experiment**: Represents a machine learning task or project, organizing related runs together.
- **Run**: A specific execution of an MLflow script that logs parameters, metrics, and artifacts.
- **Parameters**: Inputs or configurations like hyperparameters that influence the outcome of the experiment.
- **Metrics**: Evaluation measurements like accuracy or loss to assess model performance.
- **Artifacts**: Output files generated during the run, such as trained models or visualizations.
- **Tags**: User-defined metadata that can help categorize and describe experiments.

## Installation

Ensure that you have activated the correct environment (conda or venv) for your project. Then, install MLflow with:

```bash
pip install mlflow
```

## Setting Up MLflow

### Project Structure

Your project should follow a structure similar to this:

```
├── data
│   ├── Churn_Modelling.csv
└── src
    └── train.py
```

### Starting MLflow UI

To visualize and track your ML experiments, navigate to the project’s root directory and start the MLflow UI with:

```bash
mlflow ui -p 5005
```

Access the UI by visiting [http://localhost:5005](http://localhost:5005) in your browser.

### Configuring AWS S3 for Artifact Storage

To store artifacts like models and logs in AWS S3, create an S3 bucket and configure your AWS profile:

```bash
export AWS_PROFILE=mlops

aws s3api create-bucket --bucket <your-s3-bucket-name> --region <your-region> --create-bucket-configuration LocationConstraint=<your-region>
```

### Running MLflow Server with PostgreSQL Backend

To store experiment metadata in a PostgreSQL database and artifacts in the S3 bucket, start the MLflow server:

```bash
mlflow server --backend-store-uri postgresql://<user>:<password>@<your-postgres-url>:5432/<your-db-name> --default-artifact-root s3://<your-s3-bucket-name>
```

Set the `MLFLOW_TRACKING_URI` environment variable to point to the MLflow server:

```bash
export MLFLOW_TRACKING_URI=http://localhost:5000
```

## Model Registry and Deployment

MLflow also includes a **Model Registry**, which serves as a centralized model store for managing the full lifecycle of models. You can use MLflow to deploy models, including creating Docker images for deployment without having to manually create APIs.

### Building a Docker Image for the Model

Once you’ve registered a model, you can create a Docker image of it using the following command:

```bash
mlflow models build-docker --name <your-model-name> --model-uri "models:/<your-model-name>/2"
```

Run the Docker container:

```bash
docker run -d -p 8080:8080 <your-model-name>:latest
```

## References

- [MLflow Documentation](https://mlflow.org/docs/latest/model-registry.html)
- [Git Flow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [Kaggle Bank Customer Churn Dataset](https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction/data)