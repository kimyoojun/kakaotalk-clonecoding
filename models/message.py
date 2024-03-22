from sqlmodel import SQLModel, Field, Column, JSON
from typing import List

class Message(SQLModel, table=True):
  uuid: str = Field(primary_key=True, index=True)
  message: str
  participation_uuid: List[str] = Field(sa_column=Column(JSON))