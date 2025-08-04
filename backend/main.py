from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from app.routers import users

app = FastAPI()


# models.Base.metadata.create_all(bind = engine)

app = FastAPI()


MAX_RETRIES = 5
RETRY_DELAY = 3  # seconds

for attempt in range(1, MAX_RETRIES + 1):
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='think41',
            user='postgres',
            password='6369Brutal!',
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection was successful.")
        break
    except Exception as error:
        print(f"Attempt {attempt} failed: {error}")
        if attempt == MAX_RETRIES:
            print("Could not connect to the database after multiple attempts. Exiting...")
            raise  # Or use sys.exit(1) if you want to terminate the script
        print(f"Retrying in {RETRY_DELAY} seconds...\n")
        time.sleep(RETRY_DELAY)

app.include_router(users.router)