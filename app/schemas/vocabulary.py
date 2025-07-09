from pydantic import BaseModel

class VocabularyReq(BaseModel):
    title: str
    meaning: str
    sentence: str

class VocabularyRes(BaseModel):
    vocabulary_no: int
    title: str
    meaning: str
    sentence: str

    model_config = {
        "from_attributes": True
    }