from app.core.database import Async_Session

async def get_async_session():
    async with Async_Session() as session:
        yield session
        
    