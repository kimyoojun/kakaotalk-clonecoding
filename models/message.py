from sqlmodel import SQLModel, Field, Column, JSON
from typing import List, Optional

class Message(SQLModel, table=True):
  uuid: str = Field(primary_key=True, index=True)
  message: Optional[str] = None
  user_list: List[str] = Field(sa_column=Column(JSON))