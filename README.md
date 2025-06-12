# End-to-End MLOps Workflow with AWS S3, SageMaker, Lambda, & API Gateway

## Project Overview
This project demonstrates a complete machine learning pipeline using **AWS SageMaker**, showcasing how to prepare data, train a model, deploy it as an endpoint, perform inference utilizing **AWS Lambda** and **AWS API Gateway**, and then clean up resources — all programmatically from your local IDE.

## Architecture Diagram

![MLOps Architecture](assets/architecture.png)

---

## 🚀 Overview

The goal of this demo is to **learn and implement the full MLOps workflow** using AWS's managed services. It covers:

- Uploading data to the Amazon S3 bucket
- Writing a training script (`script.py`)
- Launching an AWS SageMaker training job
- Deploying the trained model as a real-time endpoint
- Accessing the endpoint using AWS Lambda
- Accessing the Lambda component using the AWS API Gateway with REST API
- Making predictions on test data through Lambda & API Gateway 
- Tearing down the model endpoint to avoid extra costs
