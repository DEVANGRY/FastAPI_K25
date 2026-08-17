from schemals.auth_schemal import FormLoginRequest
from sqlalchemy.orm import Session
from models import UserModel
from services import password_service

# FOUND_USER = "Tên tài khoản đã tồn tại"
NOT_FOUND_USER = "Tên tài khoản không tồn tại"
INCORRECT_PASSWORD = "Sai Mật Khẩu"

def handle_login_service (data_form : FormLoginRequest , db: Session):
    # Kiểm tra tài khoản đã được đăng ký chưa 
    user = db.query(UserModel).filter(UserModel.username ==  data_form.username).first()
    if not user: 
        return NOT_FOUND_USER
    
    check_password = password_service.handle_check_password(data_form.password , user.password)

    if not check_password:
        return INCORRECT_PASSWORD 

    token = password_service.handle_create_access_token(user.id, user.username , user.role.role_name) 
    return {"access_token" : token , "type_token" : "bea"}