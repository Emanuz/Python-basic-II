import os
from dotenv import load_dotenv

load_dotenv()

FLASK_APP_SECRET_KEY = os.getenv("FLASK_APP_SECRET_KEY")
TWITTER_FETCHER=os.getenv("TWITTER_FETCHER")
MLH_TWITTER_API=os.getenv("MLH_TWITTER_API")
TWITTER_URL=MLH_TWITTER_API + "/"
