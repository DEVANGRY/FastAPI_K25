import jwt
from datetime import datetime , timezone , timedelta
# Tạo hàm => Tạo ra một access_token : vé tạm thời để sử dụng hệ thống
KEY = "ajsbdjasbdasdnasdnkasdnasjadbsadasdas" 
ALO =  "HS256"

def create_access_token (user_id: str) -> str :
    now = datetime.now(timezone.utc)

    payload = {
        "sub" : user_id,
        "iat" : now,
        "exp" : now + timedelta(minutes=15)
    }

    return jwt.encode(payload=payload,key=KEY,algorithm=ALO)

print(create_access_token("hungnghichngom"))