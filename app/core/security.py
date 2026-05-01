from jose import jwt, JWTError
from fastapi import HTTPException, Header
from app.core.config import settings


def create_token(data: dict) -> str:
    return jwt.encode(
        data,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM
    )


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM]
        )
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token"
        )


def get_current_user(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    payload = decode_token(token)

    # enforce required fields (CRITICAL for multi-tenant safety)
    if "sub" not in payload or "tenant_id" not in payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token structure"
        )

    return payload