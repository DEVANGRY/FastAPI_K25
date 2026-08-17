import jwt
from datetime import datetime , timezone , timedelta

KEY = "ASJASHDAKHDKJASHDJKAHSDKJHASKDkajSHDKJSHADKJASH"
ALG = "HS256"

def create_access_token (user_id : str) -> str :
    now = datetime.now(timezone.utc)

    payload = {
        "sub" : user_id ,
        "iat" : now,
        "role" : "ADMIN",
        "exp" : now + timedelta(minutes=15)
    }

    return jwt.encode(payload,KEY,ALG)


print(create_access_token("andichoilauthe"))