from pydantic import BaseModel , Field , EmailStr , ConfigDict 
from datetime import datetime

# Lớp Pydantic Schema : Để validate dữ liệu từ client gửi tới 
class CreateAccountRequest(BaseModel):
    username : str = Field(...)
    password : str 
    email : EmailStr

class UpdateAccountRequest(BaseModel):
    username : str = Field(...)
    password : str 
    email : EmailStr
    is_status : bool


class AccountResponse(BaseModel):
    id : int 
    username : str
    email : EmailStr
    is_status : bool
    create_at : datetime

    model_config=ConfigDict(from_attributes=True)

class CreateAccountResponse(BaseModel):
    message : str
    data : AccountResponse

class GetAllAccountResponse(BaseModel):
    message : str
    data : list[AccountResponse]

class UpdateAccountResponse(BaseModel):
    message : str
    data : AccountResponse

class DeleteAccountResponse(BaseModel):
    message : str