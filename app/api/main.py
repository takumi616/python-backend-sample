from fastapi import APIRouter
from app.api.routes import vocabularies

api_router = APIRouter()
api_router.include_router(vocabularies.router)