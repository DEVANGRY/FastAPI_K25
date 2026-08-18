import bcrypt
from datetime import datetime , timezone , timedelta
import jwt 

SECRECT_KEY = "asjdhasdhsajkhsajhasjfhasjfhsajkfhdajskfbdhsfbhdsf"
ALG = "HS256"
def handle_check_password (password : str , hash_password : str) -> bool:
    return bcrypt.checkpw(password.encode() , hash_password.encode())


def handle_hash_password (password : str) -> str :
    return bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()


# Hàm để tạo token 
def handle_create_access_token (user_id : int , role_name : str , username : str) -> str:
    now_time = datetime.now(timezone.utc)

    payload = {
        "sup" : user_id ,
        "role_name" : role_name ,
        "username" : username,
        "iat" : now_time,
        "exp" : now_time + timedelta(minutes=15)
    }

    return jwt.encode(payload,SECRECT_KEY,ALG)