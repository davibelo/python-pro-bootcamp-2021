from dotenv import load_dotenv
import os
import smtplib
from twilio.rest import Client
from data_manager import DataManager

# getting actual directory and making a rel path
REL_PATH = f"{os.path.dirname(__file__)}/"

# loading environment variables
load_dotenv(dotenv_path=f"{REL_PATH}.env")


class NotificationManager:
    def __init__(self):
        self.sms_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.sms_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.dest_number = "+5581997847711"
        self.client = Client(self.sms_account_sid, self.sms_auth_token)
        self.email_bot = "davibelo.bot@gmail.com"
        self.email_password = os.getenv("EMAIL_PASSWORD")

    def send_SMS(self, text):
        print("sending SMS...")
        message = self.client.messages.create(body=text,
                                              from_="+13025664228",
                                              to=self.dest_number)
        print(f"message sid: {message.sid}")

    def send_emails(self, text):
        data_manager = DataManager()
        emails_data = data_manager.get_emails()
        dest_emails = [data["email"] for data in emails_data]

        for email in dest_emails:
            print(f"sending email to {email}...")
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.email_bot,
                                 password=self.email_password)
                connection.sendmail(
                    from_addr=self.email_bot,
                    to_addrs=email,
                    msg=f"Subject:Flight deal!\n\n{text}")
            print("email sent!")
