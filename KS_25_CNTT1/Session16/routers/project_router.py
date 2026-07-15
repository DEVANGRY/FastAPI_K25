from fastapi import APIRouter , Depends , status
from sqlalchemy.orm import Session
from database import handle_connect_DB
from services import project_service
from schemals import project_schemal


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

# Read : 
# API : Lấy tất cả dự án 
@router.get("/" , response_model=list[project_schemal.ProjectResponse], status_code=status.HTTP_200_OK)
def get_all_project(db : Session = Depends(handle_connect_DB)):
    project_db = project_service.handle_get_all_data_project(db=db)
    return project_db