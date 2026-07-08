from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy.orm import Session
from database import get_db , Base , engine
from schema import CreateUserRequest , UpdateUserRequest , UpdateDataUserResponse , UserResponse

# Import models để cấu hình toàn bộ trong database
import models
import user_service

# Chạy tạo toàn bộ các models bảng trong database
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def home(db:Session = Depends(get_db)):
    print(db)
    return {"message" : "Đây là dữ liệu trang home"}

# Code API để thêm user vào trong DATABASE
@app.post("/users")
async def create(user_new : CreateUserRequest, db:Session = Depends(get_db)):
    create_user = user_service.handle_create_user_service(db=db , user_new=user_new)

    return {"message" : "Thêm học sinh vào thành công" , "data" : create_user}


# Code API để lấy toàn bộ dữ liệu của bảng trong DATABASE
@app.get("/users") 
async def get_all_data (db:Session = Depends(get_db)):
    list_user = user_service.handle_get_all_data(db)
    return {"message": "Lấy toàn bộ dữ liệu thành công" , "data" : list_user}

# Code API để lấy toàn bộ dữ liệu của bảng trong DATABASE
@app.put("/users/{user_id}" , response_model=UpdateDataUserResponse) 
async def get_all_data (user_id : int , user_update_data : UpdateUserRequest , db:Session = Depends(get_db)):
    db_user_update = user_service.handle_update_data_user(db=db , user_id=user_id , user_update_data=user_update_data)
    if db_user_update is None :
        raise HTTPException(status_code=404 , detail="Không tìm thấy ID")
    return {"message": "Lấy toàn bộ dữ liệu thành công" , "data" : db_user_update}