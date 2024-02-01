from pprint import pprint
from  Google_api import create_service
from dotenv import load_dotenv
import os

load_dotenv()

secret_file = os.getenv("CLIENT_SECRET_FILE")
api = os.getenv("API")
version = os.getenv('VERSION')
scopes = [os.getenv("SCOPE")]

service = create_service(secret_file, api, version, scopes)

calendar = {
    'summary': 'calendarSummary',
    'timeZone': 'America/Los_Angeles'
}

created_calendar = service.calendars().insert(body=calendar).execute()

print (created_calendar['id'])