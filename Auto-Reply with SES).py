import boto3
import json

# Initialize AWS SES client
ses_client = boto3.client('ses', region_name="us-east-1")  # Change to your SES region

def lambda_handler(event, context):
    try:
        # Extract sender's email from SES event
        message = json.loads(event['Records'][0]['Sns']['Message'])
        sender_email = message['mail']['source']

        print(f"Received email from: {sender_email}")

        # Auto-reply email content
        response_email = {
            "Source": "your-email@example.com",  # Replace with your verified SES email
            "Destination": {"ToAddresses": [sender_email]},
            "Message": {
                "Subject": {"Data": "Auto-Reply: Thank you for your email"},
                "Body": {"Text": {"Data": "Hello,\n\nThank you for reaching out. We will get back to you shortly.\n\nBest Regards,\nYour Team"}}
            }
        }

        # Send the auto-reply
        ses_client.send_email(**response_email)
        print("Auto-reply sent successfully!")

    except Exception as e:
        print("Error sending auto-reply:", e)

    return {"statusCode": 200, "body": "Auto-reply processed"}
