import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
client = Client(account_sid, auth_token)


class NotificationManager:
    def __init__(self):
        self.client = client

    def send_message(self, message):
        message = self.client.messages \
            .create(
            body=message,
            from_='+17692274846',
            to='+918295484885'
        )
        print(message.sid)

    pass
