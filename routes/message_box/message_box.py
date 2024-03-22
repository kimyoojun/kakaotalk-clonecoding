from fastapi import APIRouter
from sqlmodel import Session, select, update
from starlette.responses import JSONResponse as JSON
import uuid

from db.database import engine
from models.message import Message
from models.user import User
from schemas.message import IMessage

router = APIRouter(prefix="/message", tags=["message"])

@router.post("/")
async def chatting(req:IMessage):
  with Session(engine) as session:
    useruuid = select(User).where(User.name == req.user_name)
    user_uuid_infrom = session.exec(useruuid)
    user = user_uuid_infrom.one()

    if Message.participation_uuid != req.my_uuid and Message.participation_uuid != user.uuid:

      chat_uuid = uuid.uuid1()

      participation = []
      participation.append(req.my_uuid)
      participation.append(user.uuid)

      message = Message(
        uuid=str(chat_uuid),
        participation_uuid=participation
      )

      my_chats_add = update(User).where(User.uuid == req.my_uuid).values(chats=str(chat_uuid))
      user_chats_add = update(User).where(User.uuid == user.uuid).values(chats=str(chat_uuid))

      session.add(message)
      session.exec(my_chats_add)
      session.exec(user_chats_add)
      session.commit()
  return message
    # my_chatting = select(Message).where(Message.participation_uuid == req.my_uuid and Message.participation_uuid == req.user_uuid)
    # chat_infrom = session.exec(my_chatting)
    # chat = chat_infrom.one()



@router.post("/send")
async def my_message(req: IMessage):
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
