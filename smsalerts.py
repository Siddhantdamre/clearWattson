from twilio.rest import Client

account_sid = "your_twilio_sid"
auth_token = "your_twilio_auth_token"
client = Client(account_sid, auth_token)

def send_alert(message):
    client.messages.create(
        body=message,
        from_="+your_twilio_number",
        to="+recipient_number"
    )
send_alert("Water contamination detected! pH: 7.9, Turbidity: 3.1")
