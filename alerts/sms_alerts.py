import nexmo
# Define your Nexmo API key and API secret
NEXMO_API_KEY = 'your_nexmo_api_key'
NEXMO_API_SECRET = 'your_nexmo_api_secret'
NEXMO_PHONE_NUMBER = 'your_nexmo_phone_number'  # Your Nexmo phone number
def send_sms_alert(to, message):
    client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

    response = client.send_message({
        'from': NEXMO_PHONE_NUMBER,
        'to': to,
        'text': message,
    })

    if response['messages'][0]['status'] == '0':
        print('Message sent successfully.')
    else:
        print(f"Message failed with error: {response['messages'][0]['error-text']}")

# Example usage
send_sms_alert('recipient_phone_number', 'This is a test alert from your Nexmo account.')
