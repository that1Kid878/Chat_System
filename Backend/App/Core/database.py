from .config import Database_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(Database_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
