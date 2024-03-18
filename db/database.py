from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///database.db")

async def init_db():
  SQLModel.metadata.create_all(engine)


async def drop_db():
  SQLModel.metadata.drop_all(engine)

