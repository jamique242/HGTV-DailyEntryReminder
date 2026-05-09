import boto3

sns = boto3.client('sns')

TOPIC_ARN = "replace with ARN"
print("Using Topic ARN:", TOPIC_ARN)

def lambda_handler(event, context):
    message = """
Enter our future home sweepstakes:

https://hgtv-sweepstakeslauncher-jamique.s3.us-east-1.amazonaws.com/index.html

"""

    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=message,
        Subject="Daily Sweepstakes Reminder"
    )

    return {"statusCode": 200}

