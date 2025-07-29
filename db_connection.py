import psycopg2
from config.app_config import DB_CONFIG

connection = None

def get_connection():
    global connection
    if connection is None or connection.closed:
        connection = psycopg2.connect(**DB_CONFIG)
    return connection