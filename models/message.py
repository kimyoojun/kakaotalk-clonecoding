from sqlmodel import SQLModel, Field

class Message(SQLModel, table=True):
  message: str = Field(primary_key = True)