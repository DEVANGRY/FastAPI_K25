from pydantic import BaseModel , ConfigDict

class CreateUserRequest (BaseModel):
    name_user : str 
    phone : str
    email : str
    is_active : bool

class UpdateUserRequest (BaseModel):
    name_user : str | None = None 
    phone : str | None = None
    email : str | None = None
    is_active : bool | None = None

class UserResponse(BaseModel) :
    name_user : str 
    phone : str
    email : str

    model_config=ConfigDict(from_attributes=True)

class UpdateDataUserResponse(BaseModel):
    message : str 
    data : UserResponse | None = None