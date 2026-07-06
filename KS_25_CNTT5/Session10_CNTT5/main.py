from fastapi import FastAPI , Depends
from sqlalchemy.orm import Session
from database import get_db,Base,engine
import schema
from models import CreateUserRequest
import use_service 

# Tạo thêm thực thể trong database nếu chưa có 
Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/")
def home (db: Session = Depends(get_db)):
    print(db)
    return {"message" : "TRuy xuất vào database thành công"}

# Api để thêm user vào database
@app.post("/users")
def create_user (user_create : CreateUserRequest , db : Session = Depends(get_db)):
    new_user_insert = use_service.create_user_service(db=db , user_account=user_create)
    return {"message" : "Thêm vào database thành công" , "data" : new_user_insert}

# api để lấy toàn bộ dữ liệu từ database
@app.get("/users")
def get_all_data(db : Session = Depends(get_db)):
    list_data = use_service.get_all_data_user(db=db)
    return {"message":"Lấy toàn bộ dữ liệu thành công" , "data" : list_data}