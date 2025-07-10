from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import async_engine
from app.api.main import api_router
from app.core.logger import setup_logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await async_engine.dispose()

setup_logger()

app = FastAPI()
app.include_router(api_router)