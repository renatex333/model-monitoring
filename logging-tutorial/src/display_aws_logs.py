import os
import boto3
from dotenv import load_dotenv

def main():
    load_dotenv()

    function_name = os.getenv("AWS_FUNCTION_NAME")
    lambda_group_name = f"/aws/lambda/{function_name}"

    # Initialize the AWS SDK
    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION"),
    )

    # Create a CloudWatch Logs client
    logs_client = session.client("logs")

    # Retrieve the log streams for the Lambda function
    response = logs_client.describe_log_streams(
        logGroupName=lambda_group_name
    )

    # Select the desired log stream (e.g., the latest stream)
    log_stream_name = response["logStreams"][0]["logStreamName"]
    print(f"Selected log stream: {log_stream_name}")

    # Retrieve the log events from the selected log stream
    log_events = logs_client.get_log_events(
        logGroupName=lambda_group_name,
        logStreamName=log_stream_name,
    )
    print(log_events)
    if not log_events["events"]:
        print("No log events found.")

    # Process the log events
    for i, event in enumerate(log_events["events"]):
        # Print the log event
        print(event["message"])

        # Print a separator between log events
        if event != len(log_events["events"]) - 1:
            print("-" * 60)
            print(f"LOG {i+1}:")

        # Print the log message
        print(event["message"])

if __name__ == "__main__":
    main()
