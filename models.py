from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)
from database import Base

class VerifiedFakeNews(Base):
    __tablename__ = "FakeNews"

    news_id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    news_title = Column(String, nullable=False)
    credibility = Column(Float, nullable=False)