from pydantic import BaseModel , ConfigDict
class UserBase(BaseModel):
    username : str 
    phone : str 
    age : int


class UserResponse(BaseModel):
    id : int 
    username : str 
    phone : str 
    age : int

    model_config = ConfigDict(from_attributes=True)