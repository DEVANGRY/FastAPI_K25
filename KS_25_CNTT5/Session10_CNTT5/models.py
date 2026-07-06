from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    name_user : str
    email : str 
    is_active : bool
