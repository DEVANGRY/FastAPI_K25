import jwt
from datetime import datetime,timedelta, timezone

SECRET_KEY = "ACAssasdsakdnaskdnskdnks"
ALOGORITHM = "HS256"

def create_access_token(user_id : str) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub" : str(user_id),
        "iat" : now,
        "exp" : now + timedelta(minutes=15)
    }
    return jwt.encode(payload,SECRET_KEY , algorithm=ALOGORITHM)
    
print(create_access_token("1"))