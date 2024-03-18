from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.message_box import message_box
from routes.auth import register
from routes.auth import login
from db.database import init_db, drop_db

@asynccontextmanager
async def lifespan(_app: FastAPI):
    print("API starting up")
    await init_db()
    yield
    print("API shutting down")
    await drop_db()


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",
    "http://localhost:5173/*",
]

app.add_middleware( 
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(message_box.router)
app.include_router(register.router)
app.include_router(login.router)

@app.get("/")
def read_root():
    return {"연결상태": "true"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
