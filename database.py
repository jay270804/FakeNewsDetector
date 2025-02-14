import os
from datetime import datetime
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    sessionmaker,
    DeclarativeBase,
    declared_attr,
    mapped_column,
    Mapped,
)
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# class Base(DeclarativeBase):
#     @declared_attr.directive
#     def __tablename__(cls) -> str:
#         return cls._name_.lower()

#     id: Mapped[int] = mapped_column(primary_key=True)
#     created_at: Mapped[datetime] = mapped_column(nullable=True, default=func.now())
#     updated_at: Mapped[datetime] = mapped_column(
#         nullable=True, default=func.now(), onupdate=func.now()
#     )


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()