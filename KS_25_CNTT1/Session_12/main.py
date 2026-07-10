from fastapi import FastAPI , Depends , HTTPException , status
from database import Base , engine , get_database
import models
from sqlalchemy.orm import Session
from schemas import CreateAccountRequest , CreateAccountResponse , GetAllAccountResponse , UpdateAccountRequest , UpdateAccountResponse , DeleteAccountResponse , UpdateAccountV2Request , UpdateAccountV2Response
import account_service

# Để tự động tạo các bảng trong database nếu chưa tồn tại
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Code API để thêm tài khoản người dùng vào database
@app.post("/account_user" ,response_model=CreateAccountResponse ,status_code=status.HTTP_201_CREATED)
def handle_create_account ( new_account : CreateAccountRequest, db : Session = Depends(get_database)): 
    new_account_db = account_service.create_account_service(db=db , new_account=new_account)

    if not new_account_db :
        raise HTTPException(status_code=500 , detail="Xự cố bên Server")
      
    return {"message" : "Thêm tài khoản thành công" , "data" : new_account_db}

# Code API để lấy dữ liệu từ database 
@app.get("/account_user",response_model=GetAllAccountResponse,status_code=status.HTTP_200_OK)
def handle_get_all_account(db : Session = Depends(get_database)):
    list_account_db = account_service.handle_get_all_account(db=db)
    return {"message":"Lấy danh sách thành công" , "data" : list_account_db}

# Code API để cập nhật từ database 
@app.put("/account_user/{account_id}",response_model=UpdateAccountResponse,status_code=status.HTTP_200_OK)
def handle_update_account(account_id : int , account_update : UpdateAccountRequest , db : Session = Depends(get_database)):
    account_update_db = account_service.update_account_service(db=db , account_id=account_id , update_account=account_update)
    if not account_update_db:
        raise HTTPException(status_code=404 ,detail="Không tìm thấy ID")
    return {"message" : "Cập Nhật Thành công" , "data" : account_update_db}

# Code API để xóa account từ Database
@app.delete("/account_user/{account_id}",status_code=status.HTTP_204_NO_CONTENT)
def handle_delete_account(account_id : int , db : Session = Depends(get_database)):
    is_delete_account = account_service.delete_account_service(db=db , account_id=account_id)
    if not is_delete_account:
        raise HTTPException(status_code=404 ,detail="Không tìm thấy ID")
    return 


# Code API : update - các trường bất kỳ
@app.patch("/account_user/{account_id}" , status_code=status.HTTP_200_OK , response_model=UpdateAccountV2Response)
def handle_update_acc_v2 (account_id : int , account_update :UpdateAccountV2Request , db : Session = Depends(get_database)):
    account_update_db = account_service.handle_update_account_v2_service(db=db , account_id=account_id, account_update=account_update)
    if not account_update_db:
        raise HTTPException(status_code=404 , detail="Không tìm thấy ID cần cập nhật")
    return {"message" : "Cập nhật thành công" , "data" : account_update_db}