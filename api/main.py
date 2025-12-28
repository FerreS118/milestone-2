from fastapi import FastAPI                            # Importeer FastAPI framework
from fastapi.middleware.cors import CORSMiddleware     # Middleware voor CORS (cross-origin requests)
from motor.motor_asyncio import AsyncIOMotorClient     # Async MongoDB client
import os                                              # Voor environment variables

app = FastAPI()                                        # Maak FastAPI app instance

# Voeg CORS middleware toe zodat de API toegankelijk is vanuit elke origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Haal DB configuratie op uit environment variables, met default waarden
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASS = os.getenv("DB_PASS", "apppass")
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "appdb")

# Verbinding maken met MongoDB
client = AsyncIOMotorClient(f"mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:27017")
db = client[DB_NAME]                                  # Selecteer database

# Endpoint om een gebruiker op te halen
@app.get("/")
@app.get("/user")
async def get_user():
    user = await db.users.find_one({}, {"_id": 0, "name": 1})  # Haal eerste user uit collection
    return {"name": user["name"] if user else "No user found"} # Return user naam of fallback

# Endpoint om container ID op te halen (handig bij Docker/Kubernetes)
@app.get("/container")
def get_container():
    return {"container_id": os.getenv("HOSTNAME")}    # HOSTNAME env var geeft container ID
