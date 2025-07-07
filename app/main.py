from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import async_engine, get_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await async_engine.dispose()

app = FastAPI()

@app.get("/migration-check")
async def root(db: AsyncSession = Depends(get_db)):
    try:
        query = text("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = 'vocabularies'
            )
        """)
        result = await db.execute(query)
        table_exists = result.scalar()

        if not table_exists:
            raise HTTPException(
                status_code=500, 
                detail="Table 'vocabularies' not found; migration may not have been applied"
            )
        
        return {"table_exists": True}
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB health check failed: {str(e)}")
