from fastapi import APIRouter , Depends , HTTPException ,status , Form , UploadFile , File
from schemals.auth_schemal import FormLoginRequest , LoginResponse
from sqlalchemy.orm import Session
from database import connect_db
from services  import auth_service
from fastapi.staticfiles import StaticFiles
import os , uuid , shutil

auth_router = APIRouter(prefix="/auth",tags=["Auth"])

# API : LOGIN
@auth_router.post("/login" , response_model=LoginResponse , status_code=status.HTTP_200_OK)
def handle_login (data_form : FormLoginRequest , db: Session = Depends(connect_db)):
    data = auth_service.handle_login_service(data_form=data_form , db=db)

    if data == auth_service.NOT_FOUND_USER:
        raise HTTPException(
            status_code=404,
            detail="Không tìm thấy tài khoản"
        )
    else :
        return data

    
@auth_router.post("/login_v2")
def handle_login_v2(
    username : str = Form(...),
    password : str = Form(...)
):
    # login 
    return {"message" : "Đăng nhập thành công" , "username" : username , "password" : password}



DIR_UPLOAD_FILE = "upload/images"
os.makedirs(DIR_UPLOAD_FILE,exist_ok=True)

# Xây dựng một api làm việc với file , uploadfile , và lưu ảnh vào một folder tĩnh của dự án
@auth_router.post("/upload_file_image")
def handle_upload_image (file_image : UploadFile = File(...)):
    # Kiểm tra xem file có phải file ảnh không
    # Lấy đường dẫn cuối cùng trong ảnh 
    type_img = file_image.filename.split(".")[-1]
    if type_img != "png":
        raise HTTPException(status_code=400)

    # đặt lại tên ảnh cho đúng quy chuẩn hệ thống
    new_name_file = f"{uuid.uuid4().hex}.{type_img}"

    # Tạo URL trực tiếp  của ảnh này 
    url_image_create = os.path.join(DIR_UPLOAD_FILE,new_name_file)
    # upload/images/8be41a7273a344b0af64975e702b9e74.png

    # Lưu lại ảnh vào folder tĩnh mà mình đã tạo
    with open(url_image_create,"wb") as buffer:
        shutil.copyfileobj(file_image.file,buffer)

    return file_image