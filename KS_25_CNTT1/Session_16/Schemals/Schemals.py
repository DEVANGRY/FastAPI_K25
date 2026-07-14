from pydantic import BaseModel , ConfigDict
class ProjectBase (BaseModel) :
    project_name : str 
    technology : str
    day : int


class ProjectResponse(ProjectBase) :
    id : int
    student_id : int
    model_config = ConfigDict(from_attributes=True)

class StudentBase (BaseModel) :
    name : str 
    email : str


class StudentResponse(StudentBase) :
    id : int 
    projects : list[ProjectResponse]
    model_config = ConfigDict(from_attributes=True)
