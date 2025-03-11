from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv


load_dotenv() 


def is_running_in_docker():
    return os.path.exists("/.dockerenv") or "DOCKER" in os.environ


DB_HOST = "db" if is_running_in_docker() else os.getenv("DB_HOST", "localhost")

DB_URL = f"mariadb+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{DB_HOST}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
