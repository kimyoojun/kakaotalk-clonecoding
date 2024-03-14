from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///database.db")

def init_db():
  SQLModel.metadata.create_all(engine)

