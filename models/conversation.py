from sqlalchemy import Column, Integer, String, Text, DateTime

from db.database import Base

class conversation(Base):
    __tablename__ = "conversation"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)