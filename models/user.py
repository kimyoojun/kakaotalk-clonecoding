from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
  name: str = Field(index=True)
  email: str = Field(unique=True)
  id: str = Field(primary_key=True, index=True)
  pw: str
  token: str