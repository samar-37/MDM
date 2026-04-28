def lambda_handler(event, context):
    password = NONE  # Vulnerability for testing
    return {
        'statusCode': 200,
        'body': 'Hello Secure CI/CD'
    }
