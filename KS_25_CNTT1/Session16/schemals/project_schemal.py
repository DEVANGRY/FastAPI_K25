from pydantic import BaseModel , ConfigDict
from .user_schemal import UserResponse

class ProjectBase (BaseModel):
    project_name : str 
    technology : str 
    day : int 
    project_detail : str 

class ProjectResponse(BaseModel):
    id : int 
    project_name : str 
    technology : str 
    day : int 
    project_detail : str 
    user :  UserResponse

    model_config = ConfigDict(from_attributes=True)

