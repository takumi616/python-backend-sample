from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.models.vocabulary import Vocabulary
from app.schemas.vocabulary import VocabularyReq


async def find_all(db: AsyncSession) -> list[Vocabulary]:
    result = await db.execute(select(Vocabulary))
    vocabularies = result.scalars().all()

    return vocabularies

async def find_by_no(vocabulary_no: int, db: AsyncSession) -> Vocabulary:
    result = await db.execute(select(Vocabulary).filter(Vocabulary.vocabulary_no == vocabulary_no))
    vocabulary = result.scalars().first()
    
    return vocabulary

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
