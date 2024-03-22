from pydantic import BaseModel, Field
from typing import Optional

class IMessage(BaseModel):
  message: Optional[str] = None
  my_uuid: str
  user_name: str
