from fastapi import APIRouter , Depends ,status , HTTPException
from sqlalchemy.orm import Session
from database import handle_connect_DB
from services import project_service
from Schemas import project_schema
#  Tạo bộ định tuyến 
router_project = APIRouter(prefix="/projects",tags=["Project"])


# API lấy dữ liệu 
@router_project.get("/",response_model=list[project_schema.ProjectResponse] ,status_code=status.HTTP_200_OK)
def get_all_project (db : Session = Depends(handle_connect_DB)):
    list_project_db = project_service.handle_get_all_data_project_service(db=db)
    return list_project_db

# API để xóa dự án 
@router_project.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project (project_id : int , db : Session = Depends(handle_connect_DB)):
    is_delete = project_service.handle_delete_project_by_id_service(project_id=project_id,db=db)
    if is_delete == "NOT_FOUND_PROJECT":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Không tìm thấy ID dự án")
    return 

# API để thêm dự án 
@router_project.post("/", response_model=project_schema.ProjectResponse,status_code=status.HTTP_201_CREATED)
def create_project (payload : project_schema.ProjectRequest ,db : Session = Depends(handle_connect_DB)):
    new_project_db = project_service.handle_create_project_service(payload=payload,db=db)
    if new_project_db == "NOT_FOUND_USER":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Không tìm thấy ID người dùng")
    return new_project_db

# API để cập nhật
@router_project.put("/{project_id}", response_model=project_schema.ProjectResponse,status_code=status.HTTP_200_OK)
def create_project (project_id : int ,payload : project_schema.ProjectRequest ,db : Session = Depends(handle_connect_DB)):
    new_project_update_db = project_service.handle_update_project_service(project_id=project_id , payload=payload,db=db)
    if new_project_update_db == "NOT_FOUND_USER":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Không tìm thấy ID người dùng")
    elif new_project_update_db == "NOT_FOUND_PROJECT":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Không tìm thấy ID dự án")
    return new_project_update_db