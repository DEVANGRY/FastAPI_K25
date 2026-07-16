from pydantic import BaseModel , ConfigDict
class UserResponse (BaseModel):
    id : int 
    username : str
    phone : str 
    age : int 

    model_config = ConfigDict(from_attributes=True)