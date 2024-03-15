from pydantic import BaseModel, Field

class IRegister(BaseModel):
  name: str = Field(...)
  email: str = Field(...)
  id: str = Field(...)
  pw: str = Field(...)