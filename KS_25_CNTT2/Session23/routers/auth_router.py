from fastapi import APIRouter , Depends , status
from sqlalchemy.orm import Session
from schemals.auth_schemal import RegisterRequest , RegisterReponse , LoginRequest , LoginResponse
from database import get_db
from services import auth_service

auth_router = APIRouter(prefix="/auth",tags=["Authentication"])

# Register
@auth_router.post("/register" , response_model=RegisterReponse , status_code= status.HTTP_201_CREATED)
def handle_register_account(form_account : RegisterRequest , db : Session = Depends(get_db)):
    response_data = auth_service.handle_register_service(form_account=form_account , db=db)

    return {"message" : "Đăng ký tài khoản thành công"}

# login 
@auth_router.post("/login",response_model=LoginResponse , status_code= status.HTTP_200_OK)
def handle_login_account(form_account : LoginRequest , db : Session = Depends(get_db)):
    response_data = auth_service.handle_login_service(form_account=form_account,db=db)

    return {"message" : "Đăng nhập thành công" , "access_token" : response_data , "type_token" : "bearer"}


# Get_user_info :lấy token mà người dùng đã đăng nhập thành công sau đó mã hóa ngược lại 
# để lấy dữ liệu trong payload
@auth_router.get("/get_user")
def handle_get_data_user (user : dict = Depends(auth_service.get_data_user)):
    return user

@auth_router.get("/list_all",dependencies=[Depends(auth_service.CheckRole(["Admin"]))])
def handle_get_all_data ():
    return {"message" : "toàn bộ dữ liệu"}