from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name: str
    prompt: str


class ProjectOut(BaseModel):
    id: str
    name: str
    prompt: str
    tenant_id: str

    class Config:
        from_attributes = True