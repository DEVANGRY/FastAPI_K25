from fastapi import APIRouter , Depends , status, HTTPException
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

# Create : Thêm dự án 
@router.post("/",response_model=project_schemal.ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project ( payload : project_schemal.CreateProjectRequest,db : Session = Depends(handle_connect_DB)):
    create_project_db = project_service.handle_create_project(db=db , payload=payload)
    if not create_project_db :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Không tìm thấy ID người dùng")
    
    return create_project_db

# Delete : Xóa dự án 
@router.delete("/{project_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id : int , db : Session = Depends(handle_connect_DB)):
    is_delete_project = project_service.handle_delete_project(db=db , project_id=project_id)
    if not is_delete_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Không tìm thấy ID dự án")
    return

# Create : cập nhật dự án 
@router.patch("/{project_id}",response_model=project_schemal.UpdateProjectResponse, status_code=status.HTTP_200_OK)
def update_project ( project_id: int , payload : project_schemal.UpdateProjectRequest,db : Session = Depends(handle_connect_DB)):
    new_update_project = project_service.handle_update_project(db=db , project_id=project_id , payload=payload)
    if new_update_project == "NOT_FOUND_USER":
        raise
    elif new_update_project == "NOT_FOUND_PROJECT":
        raise
    else:
        return new_update_project