from sqlalchemy.orm import Session
from schemals.auth_schemal import RegisterRequest , LoginRequest
from models import UserModel
from utils import security
from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials
from fastapi import Depends , HTTPException
import jwt 

FOUND_ACCOUNT = "Tài khoản đã được lập trước đó"
FOUND_EMAIL = "Email đã tồn tại"
def handle_register_service (form_account : RegisterRequest , db : Session):

    # Kiểm tra username có tồn tại không 
    user = db.query(UserModel).filter(UserModel.username == form_account.username).first()

    if user : 
        return FOUND_ACCOUNT
    
    # Kiểm tra email có trùng không 
    user = db.query(UserModel).filter(UserModel.email == form_account.email).first()
    if user : 
        return FOUND_EMAIL

    # hash password : Băm mật khẩu 
    hash_password = security.handle_hash_password(form_account.password)

    # Tạo một bản ghi mới UserModel
    new_account = UserModel(
        username = form_account.username,
        password = hash_password,
        email = form_account.email ,
        role_id = 3
    )

    # .add , .commit , .refesh
    db.add(new_account)

    db.commit()

    db.refresh(new_account)
    
    return new_account




def handle_login_service (form_account : LoginRequest , db : Session):
    # Kiểm tra tài khoản có tồn tại hay không 
    user = db.query(UserModel).filter(UserModel.username == form_account.username).first()

    # Kiểm tra password 
    is_correct_password = security.handle_check_password(form_account.password , user.password)

    # Tạo access_token 
    token = security.handle_create_access_token(user.id,user.role.role_name ,user.username)

    # return access_token

    return token

security_token = HTTPBearer()

def get_data_user (crendetials :HTTPAuthorizationCredentials = Depends(security_token)):
    token = crendetials.credentials

    try:
        payload = jwt.decode(token,security.SECRECT_KEY,security.ALG)
        username  = payload.get("username")
        role_name = payload.get("role_name")
        return {"username" :username , "role_name" : role_name}
    
    except jwt.ExpiredSignatureError:
      return "Lỗi chữ ký hết hạn"


class CheckRole:
    def __init__(self, allow_roles):
        self.allow_roles = allow_roles

    def __call__(self , user : dict = Depends(get_data_user)):
        if user.get("role_name") not in self.allow_roles:
            raise HTTPException(
                status_code=403,
                detail=f"Quyển của tài khoản không đủ thẩm quyền truy cập"
            )
        return user