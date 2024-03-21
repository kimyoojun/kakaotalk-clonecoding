from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
  name: str = Field(index=True)
  email: str = Field(unique=True)
  id: str = Field(primary_key=True, index=True)
  pw: str
  token: str
  friends: Optional[str] = None 
  chats: Optional[str] = None 