from pydantic import BaseModel, Field
from typing import Optional

class IRegister(BaseModel):
  name: str = Field(...)
  email: str = Field(...)
  id: str = Field(...)
  pw: str = Field(...)
  token: Optional[str] = None 

class ILogin(BaseModel):
  id: str = Field(...)
  pw: str = Field(...)