from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RADARIO_QUERY_URL = os.getenv('RADARIO_QUERY_URL')
RADARIO_QUERY_KEY = os.getenv('RADARIO_QUERY_KEY')
# В секундах
UPDATE_TIME_INTERVAL = os.getenv('UPDATE_TIME_INTERVAL')
THEATRE_URL = os.getenv('THEATRE_URL')
THEATRE_EVENT_URL = os.getenv('THEATRE_EVENT_URL')
THEATRE_DB_NAME = os.getenv('THEATRE_DB_NAME') or 'theatre.db'
THEATRE_DB_PATH = os.getenv('THEATRE_DB_PATH') or os.path.dirname(__file__) + '/' + THEATRE_DB_NAME
