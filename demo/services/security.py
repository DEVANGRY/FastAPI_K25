import bcrypt 
from datetime import datetime , timezone , timedelta
from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials
from fastapi import Depends
import jwt 
from sqlalchemy.orm import Session
from database import handle_connect_db
from models import RoleModel

SECRET_KEY = "asjdaslhdashdasjdhasjdhasljdahsjldhasd"
ALG = "HS256"

security_token = HTTPBearer()

def verify_password (raw_password: str , hash_password) -> bool:
    return bcrypt.checkpw(raw_password.encode() , hash_password.encode())


def create_access_token (username : str , role_id : int) -> str: 
    now = datetime.now(timezone.utc)
    payload = {
        "sub" : str(username),
        "role_id" : role_id,
        "iat" : now ,
        "exp" : now + timedelta(minutes=15)
    }

    return jwt.encode(payload,SECRET_KEY, ALG)

# Hàm xác thực người dùng 

def get_current_user (credentials :HTTPAuthorizationCredentials = Depends(security_token)):
    # bóc lấy chuỗi token 
    token = credentials.credentials

    try:
        payload = jwt.decode(token,SECRET_KEY,ALG)
        username = payload.get("sub")
        role_id = payload.get("role_id")
        if username is None :
            return "TOKEN KHÔNG HỢP LỆ"
        return {"username" : username , "role_id" : role_id}
    except jwt.ExpiredSignatureError:
        return "TOKEN HẾT HẠN"
    except jwt.InvalidTokenError:
             return "Token giả mạo" 

# Lớp Phân Quyền 
class RoleChecker:
    def __init__(self,allowed_role : list):
        self.allowed_role = allowed_role

    def __call__(self , user:dict = Depends(get_current_user), db : Session = Depends(handle_connect_db)):
        user_role_name = db.query(RoleModel).filter(RoleModel.id == user["role_id"]).first().role_name
        if user_role_name not in self.allowed_role:
             return "Quyền không được phép thực hiện chức năng này"
        return user