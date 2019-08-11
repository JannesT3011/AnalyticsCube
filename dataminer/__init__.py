from datetime import datetime
utcnow = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

from .bot_data import bot_requests, bot_messages
from .mentions import mentions_data