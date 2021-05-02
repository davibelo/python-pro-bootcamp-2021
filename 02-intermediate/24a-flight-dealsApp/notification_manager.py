from dotenv import load_dotenv
import os
from twilio.rest import Client

# getting actual directory and making a rel path
REL_PATH = f"{os.path.dirname(__file__)}/"

# loading environment variables
load_dotenv(dotenv_path=f"{REL_PATH}.env")

class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.dest_number = "+5581997847711"
        self.client = Client(self.account_sid, self.auth_token)

    def send_SMS(self, text):

        print("sending SMS...")
        message = self.client.messages.create(
            body=text,
            from_="+13025664228",
            to=self.dest_number
        )
        print(f"message sid: {message.sid}")