from datetime import datetime
utcnow = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
year = datetime.utcnow().strftime("%Y")
month = datetime.utcnow().strftime("%Y-%m")
today = datetime.utcnow().strftime("%Y-%m-%d")

from .bot_data import bot_requests, bot_messages
from .mentions import mentions_data