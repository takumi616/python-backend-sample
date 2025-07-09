from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.models.vocabulary import Vocabulary
from app.schemas.vocabulary import VocabularyReq


async def create(req: VocabularyReq, db: AsyncSession) -> Vocabulary:
    vocabulary = Vocabulary(
        title=req.title,
        meaning=req.meaning,
        sentence=req.sentence
    )

    db.add(vocabulary)
    await db.commit()
    await db.refresh(vocabulary)
    
    return vocabulary
