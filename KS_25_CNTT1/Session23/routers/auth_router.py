from fastapi import APIRouter , Depends , HTTPException ,status
from schemals.auth_schemal import FormLoginRequest , LoginResponse
from sqlalchemy.orm import Session
from database import connect_db
from services  import auth_service

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