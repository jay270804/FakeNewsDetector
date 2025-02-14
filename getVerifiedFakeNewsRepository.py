from sqlalchemy import inspect, func
from typing import List
from database import Base
from models import VerifiedFakeNews
from sqlalchemy.orm import Session

def get_verified_news_data(db: Session) -> List[VerifiedFakeNews]:
    # Create an inspector to check if the table exists
    inspector = inspect(db.get_bind())

    # Check if the table exists
    if not inspector.has_table(VerifiedFakeNews.__tablename__):
        # If the table doesn't exist, create it
        Base.metadata.create_all(db.get_bind())

    return db.query(VerifiedFakeNews).order_by(func.random()).limit(5).all()

def store_fake_news_data(db: Session, news_title: str, confidence: float) -> None:
    # Create a new instance of VerifiedFakeNews
    fresh_news = VerifiedFakeNews(news_title=news_title, confidence=confidence)
    print("after fresh_news creation")
    # Add the new instance to the session
    db.add(fresh_news)
    print("after fresh_news add")

    # Commit the session to save the new record to the database
    db.commit()
    print("after fresh_news commit")

    # Refresh the instance to get any database-generated values (e.g., autoincrement ID)
    db.refresh(fresh_news)
    print("after fresh_news refresh")