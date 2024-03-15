from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.message_box import message_box
from db.database import init_db
from routes.auth import register

app = FastAPI()

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

@app.get("/")
def read_root():
    return {"연결상태": "true"}

if __name__ == "__main__":
    init_db()

