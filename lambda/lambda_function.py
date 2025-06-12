import json
import os
import boto3

# Initialize SageMaker runtime client
sm_client = boto3.client('sagemaker-runtime')

# Endpoint name of your deployed model
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']

def lambda_handler(event, context):
    # Extract input data from the event (assume it's JSON)
    input_data = event.get('body')
    
    # If input_data is a string (like from API Gateway), parse it first
    if isinstance(input_data, str):
        input_data = json.loads(input_data)
    
    # Now, input_data is likely a list or dict — convert to string, then bytes
    payload_str = json.dumps(input_data)
    payload_bytes = payload_str.encode('utf-8')
    
    # Call SageMaker endpoint to get predictions
    response = sm_client.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType='application/json',  # or 'text/csv' depending on your model input
        Body=payload_bytes
    )
    
    # Read response body and decode it
    result = response['Body'].read().decode('utf-8')
    
    # Return the result to the API Gateway or client
    return {
        'statusCode': 200,
        'body': result
    }
