# AWS SageMaker End-to-End Model Deployment Workflow

![AWS Sagemaker](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAjJJVP5yFl_6XgEwFSzBz7KcZsNL2XAclOA&s)

This project demonstrates a complete machine learning pipeline using **AWS SageMaker**, showcasing how to prepare data, train a model, deploy it as an endpoint, perform inference, and clean up resources — all programmatically from your local IDE.

---

## 🚀 Overview

The goal of this demo is to **learn and implement the full ML workflow** using SageMaker's managed services. It covers:

- Uploading data to Amazon S3
- Writing a training script (`script.py`)
- Launching a SageMaker training job
- Deploying the trained model as a real-time endpoint
- Making predictions on test data
- Tearing down the endpoint to avoid extra costs
