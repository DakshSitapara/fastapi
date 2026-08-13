# import os
# import time

# import psycopg2
# import psycopg2.extras

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

DB_HOST = settings.database_host
DB_NAME = settings.database_name
DB_USER = settings.database_user
DB_PASSWORD = settings.database_password
DB_PORT = settings.database_port

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



# while True:
#     try:
#         conn = psycopg2.connect(
#             host=os.getenv("DATABASE_HOST", "localhost"),
#             database=os.getenv("DATABASE_NAME", "fastapi"),
#             user=os.getenv("DATABASE_USER", "postgres"),
#             password=os.getenv("DATABASE_PASSWORD", "12345678"),
#             port=os.getenv("DATABASE_PORT", "5432"),
#             cursor_factory=psycopg2.extras.RealDictCursor,
#         )
#         conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error:", error)
#         time.sleep(2)