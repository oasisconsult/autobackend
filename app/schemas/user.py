from pydantic import BaseModel


class UserOut(BaseModel):
    id: str
    email: str
    tenant_id: str

    class Config:
        from_attributes = True