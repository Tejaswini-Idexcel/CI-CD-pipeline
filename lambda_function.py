import json

def lambda_handler(event, context):
    """
    Sample pure Lambda function that returns a message AND the event body
    """
    print(f"Received event: {json.dumps(event)}")
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from AWS Lambda CI/CD Pipeline!",
            "input": event
        })
    }
