from app.core.security import create_token, decode_token


def test_token_flow():
    token = create_token({"sub": "123", "tenant_id": "t1"})

    payload = decode_token(token)

    assert payload["sub"] == "123"