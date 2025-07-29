import psycopg2
from config.app_config import DB_CONFIG

CREATE_USERS_TABLE_SQL = '''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
'''

CREATE_HEALTH_ANALYSIS_TABLE_SQL = '''
CREATE TABLE IF NOT EXISTS health_analysis (
    id SERIAL PRIMARY KEY,
    user_email VARCHAR(255) NOT NULL,
    symptoms TEXT NOT NULL,
    analysis TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

def setup_database():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute(CREATE_USERS_TABLE_SQL)
    cur.execute(CREATE_HEALTH_ANALYSIS_TABLE_SQL)
    conn.commit()
    cur.close()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database() 