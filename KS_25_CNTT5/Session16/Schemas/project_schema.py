from pydantic import BaseModel , ConfigDict
from .user_schema import UserResponse

class ProjectResponse (BaseModel):
    id : int 
    project_name : str 
    technology : str 
    day : int 
    project_detail : str 
    user : UserResponse

    model_config = ConfigDict(from_attributes=True)

class ProjectRequest (BaseModel):
    project_name : str 
    technology : str 
    day : int 
    project_detail : str 
    user_id : int 