from pydantic import BaseModel

class CreateUserRequest (BaseModel):
    name_user : str 
    phone : str
    email : str
    is_active : bool