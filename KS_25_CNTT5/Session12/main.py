from fastapi import FastAPI , status , Depends , HTTPException
from database import Base , engine , handle_connect_DB
import models
from schemas import CreateAccountRequest , CreateAccountResponse , GetAllAccountResponse , UpdateAccountRequest , UpdateAccountResponse , DeleteAccountResponse
from sqlalchemy.orm import Session
import account_service

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Tạo API để thêm tài khoản người dùng vào DATABASE 
@app.post("/account-user",status_code=status.HTTP_201_CREATED , response_model=CreateAccountResponse)
def create_account_user(new_account : CreateAccountRequest , db : Session = Depends(handle_connect_DB)) :
    new_account_db = account_service.handle_create_account_service(db=db , new_account=new_account)
    return {"message" : "Thêm dữ liệu thành công" , "data" : new_account_db }

# Tạo API lấy toàn bộ tài khoản người dùng DATABASE
@app.get("/account-user" ,status_code=status.HTTP_200_OK , response_model=GetAllAccountResponse)
def get_all_account_user(db : Session = Depends(handle_connect_DB)) :
    list_account_db = account_service.handle_get_all_account_service(db=db)
    return {"message": "Lấy toàn bộ dữ liệu thành công" , "data" : list_account_db}

# Tạo API để update tài khoản người dùng 
@app.put("/account-user/{account_id}" ,status_code=status.HTTP_200_OK , response_model=UpdateAccountResponse)
def update_account_user(account_id:int , data_update_account : UpdateAccountRequest , db : Session = Depends(handle_connect_DB)):
    find_account_user_db = account_service.handle_update_account_service(db=db ,account_id=account_id , data_update_account= data_update_account)

    if not find_account_user_db :
        raise HTTPException(status_code=404 , detail="Không tìm thấy tài khoản người dùng")
    return {"message" :"Cập Nhật Thành công" , "data" : find_account_user_db}

# Tạo API để xóa tài khoản 
@app.delete("/account-user/{account_id}" ,status_code=status.HTTP_204_NO_CONTENT )
def delete_account_user(account_id:int , db : Session = Depends(handle_connect_DB)):
    is_delete_success = account_service.handle_delete_account_service(db=db ,account_id=account_id )
    if not is_delete_success :
        raise HTTPException(status_code=404 , detail="Không tìm thấy tài khoản người dùng")
    return