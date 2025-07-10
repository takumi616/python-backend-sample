import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, DataError
from typing import Any
from app.dependencies import get_async_session
from app.models.vocabulary import Vocabulary
from app.schemas.vocabulary import VocabularyReq, VocabularyRes
from app.crud import vocabulary as crud

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/vocabularies", tags=["vocabularies"])

@router.get("/{vocabulary_no}", response_model=VocabularyRes, status_code=status.HTTP_200_OK)
async def get_vocabulary_by_no(vocabulary_no: int, db: AsyncSession = Depends(get_async_session)) -> Any:
    fetched = await crud.find_by_no(vocabulary_no, db)

    return VocabularyRes.model_validate(fetched)

@router.post("", response_model=VocabularyRes, status_code=status.HTTP_201_CREATED)
async def create_vocabulary(req: VocabularyReq, db: AsyncSession = Depends(get_async_session)) -> Any:
    try:
        created = await crud.create(req, db)

        return VocabularyRes.model_validate(created)

    except IntegrityError as e:
        logger.error(f"Integrity error: {e.orig}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The vocabulary already exists."
        )

    except Exception as e:
        logger.error(f"Unexpected error during vocabulary creation: {e.orig}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="The vocabulary could not be registered."
        )






