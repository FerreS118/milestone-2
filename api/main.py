from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_USER = os.getenv("DB_USER", "appuser")
DB_PASS = os.getenv("DB_PASS", "apppass")
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "appdb")

client = AsyncIOMotorClient(f"mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:27017")
db = client[DB_NAME]
@app.get("/")
@app.get("/user")
async def get_user():
    user = await db.users.find_one({}, {"_id": 0, "name": 1})
    return {"name": user["name"] if user else "No user found"}

@app.get("/container")
def get_container():
    return {"container_id": os.getenv("HOSTNAME")}
