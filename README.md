# End-to-End MLOps Workflow with AWS S3, SageMaker, Lambda, & API Gateway

## 🚀 Project Overview
This project demonstrates a complete machine learning pipeline using **AWS SageMaker**, showcasing how to prepare data, train a model, deploy it as an endpoint, perform inference utilizing **AWS Lambda** and **AWS API Gateway**, and then clean up resources — all programmatically from your local IDE.

This demo covers:

- Uploading data to the Amazon S3 bucket
- Writing a training script (`script.py`)
- Launching an AWS SageMaker training job
- Deploying the trained model as a real-time endpoint
- Accessing the endpoint using AWS Lambda
- Accessing the Lambda component using the AWS API Gateway with REST API
- Making predictions on test data through Lambda & API Gateway 
- Tearing down the model endpoint to avoid extra costs

## 📊 Architecture Diagram

![MLOps Architecture](assets/architecture.png)

---

## 🧠 Key Learnings

1. End-to-End Machine Learning Lifecycle on AWS
- Understood and implemented the full ML pipeline:
  - Data preprocessing
  - Model training
  - Model evaluation
  - Deployment to a real-time endpoint
"Learned to take a raw dataset from CSV all the way to a production-ready inference pipeline using AWS."

2. SageMaker Hands-on
- Used SageMaker’s built-in XGBoost estimator
- Uploaded datasets and models to Amazon S3
- Trained and deployed a model using SageMaker Estimator API
- Created and invoked a SageMaker real-time endpoint
"Explored model versioning, cloud storage for data/model artifacts, and deployment best practices."



