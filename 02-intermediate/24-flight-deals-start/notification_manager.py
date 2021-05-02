from dotenv import load_dotenv()
from twilio.rest import Client

# getting actual directory and making a rel path
REL_PATH = f"{os.path.dirname(__file__)}/"

# loading environment variables
load_dotenv(dotenv_path=f"{REL_PATH}.env")

# SMS API information

client = Client(account_sid, auth_token)


class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.dest_number = "+5581997847711"
        