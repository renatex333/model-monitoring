import os
import io
import json
import boto3
import requests
from dotenv import load_dotenv

def test_function(lambda_client, function_name):

    assert function_exists(lambda_client, function_name) is True, f"Function {function_name} does not exist"

    response = function_invoke(lambda_client, function_name)
    response = json.loads(response)
    print(response)

def function_exists(lambda_client, function_name) -> bool:
    """
    Check if the function exists
    """
    try:
        lambda_client.get_function(FunctionName=function_name)
        return True
    except lambda_client.exceptions.ResourceNotFoundException:
        return False
    
def function_invoke(lambda_client, function_name) -> dict:
    """
    Invoke the function
    """
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType="RequestResponse",
    )

    payload = response["Payload"]

    return io.BytesIO(payload.read()).read().decode("utf-8")

if __name__ == "__main__":
    load_dotenv()

    # Create a Boto3 client for AWS Lambda
    lambda_client = boto3.client(
        "lambda",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION"),
    )

    test_function(lambda_client, "do_something_concurrent_renatex")
