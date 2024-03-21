from pydantic import BaseModel, Field

class IMessage(BaseModel):
  message: str

