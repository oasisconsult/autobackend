from pydantic import BaseModel


class GenerationRequest(BaseModel):
    prompt: str


class GenerationOut(BaseModel):
    id: str
    status: str
    score: int | None

    class Config:
        from_attributes = True