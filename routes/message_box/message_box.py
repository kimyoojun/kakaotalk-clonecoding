from fastapi import APIRouter
from sqlmodel import Session, select
from starlette.responses import JSONResponse as JSON

from db.database import engine
from models.message import Message
from schemas.speech import Imessage

router = APIRouter(prefix="/message", tags=["message"])

@router.post("/")
async def my_message(req: Imessage):
  if not req.message:
    return JSON({"msg": "메세지를 입력해주세요."}, 400)
  
  message = Message(
    message = req.message
  )

  try:
    with Session(engine) as session:
      session.add(message)
      session.commit()
  except Exception as e:
    print(e)
    return JSON({"msg": "메세지 전송에 실패하였습니다."}, 500)
  finally:
    return JSON({"msg": "메세지전송에 성공하였습니다"}, 200)
  
@router.get("/window/")
async def message_window():
  with Session(engine) as session:
    message_table = select(Message)
    message_value = session.exec(message_table).all()
    last_message = message_value[-1]
    print(last_message)
  return last_message
