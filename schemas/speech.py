from pydantic import BaseModel, Field

class Imessage(BaseModel):
  message: str