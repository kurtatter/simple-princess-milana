from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RADARIO_QUERY_URL = os.getenv('RADARIO_QUERY_URL')
RADARIO_QUERY_KEY = os.getenv('RADARIO_QUERY_KEY')
UPDATE_TIME_INTERVAL = os.getenv('UPDATE_TIME_INTERVAL')
