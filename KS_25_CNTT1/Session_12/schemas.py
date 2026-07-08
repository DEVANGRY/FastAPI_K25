#  Đây là cấu hình của các data được đẩy lên từ client 
from pydantic import BaseModel , ConfigDict

class CreateAccountRequest(BaseModel):
    account : str
    password : str
    email : str
    is_active : bool

class UpdateAccountRequest(BaseModel):
    account : str
    password : str
    email : str
    is_active : bool


class AccountResponse(BaseModel):
    account : str
    email : str
    is_active : bool
    id: int

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