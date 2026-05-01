from fastapi import Header, HTTPException
from app.core.security import decode_token


def get_current_user(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    payload = decode_token(token)

    if "sub" not in payload:
        raise HTTPException(status_code=401, detail="Missing user id")

    if "tenant_id" not in payload:
        raise HTTPException(status_code=401, detail="Missing tenant id")

    return payload


def get_tenant_id(user=Header(...)):
    return user["tenant_id"]