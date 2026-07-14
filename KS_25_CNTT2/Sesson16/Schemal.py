from pydantic import BaseModel , ConfigDict

class DepartmentInfo (BaseModel):
    id : int 
    name : str
    model_config = ConfigDict(from_attributes=True)

class CourseInfo (BaseModel):
    id : int 
    name : str
    model_config = ConfigDict(from_attributes=True)

class StudentDetailInfo (BaseModel):
    id : int 
    full_name : str 
    status : str 
    department : DepartmentInfo
    courses : list[CourseInfo] 