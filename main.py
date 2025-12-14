from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(
    debug=True,
    lifespan=lifespan
)

@app.get("/")
async def home():
    return {"message": "Hello"}