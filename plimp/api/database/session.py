from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from dotenv import load_dotenv


load_dotenv()
DB_CONNECTION_URL = os.getenv("DB_CONNECTION_URL")

engine = create_engine(
    DB_CONNECTION_URL,
    pool_size=20,
    max_overflow=2,
    pool_timeout=30,
    pool_recycle=300,
    pool_pre_ping=True,
    pool_use_lifo=True,
    connect_args={
        "keepalives": 1,
        "keepalives_idle": 30,
        "keepalives_interval": 10,
        "keepalives_count": 5,
    },
)

sessionLocal = sessionmaker(bind=engine)


# For FastAPI
def get_session():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


# For tools / scripts
def get_tools_session():
    return sessionLocal()
