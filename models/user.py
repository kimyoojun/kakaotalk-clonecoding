from sqlmodel import SQLModel, Field, Column, JSON
from typing import List,Optional

class User(SQLModel, table=True):
  name: str = Field(index=True)
  email: str = Field(unique=True)
  id: str = Field(primary_key=True, index=True)
  pw: str
  token: str
  friends: List[str] = Field(sa_column=Column(JSON))
  chats: Optional[str] = None