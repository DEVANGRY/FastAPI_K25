from fastapi import APIRouter , Depends , status ,HTTPException
from sqlalchemy.orm import Session
from database import handle_connect_DB
import Services.project_service as project_service 
import Schemals.Project as ProjectSchema

router = APIRouter(prefix="/projects",tags=["Projects"])
# Read : 
# lấy toàn bộ dự án , phân trang 
# lấy dự án theo ID người dùng 

@router.get("/get-all" , response_model=list[ProjectSchema.ProjectResponse])
async def get_all(db: Session = Depends(handle_connect_DB)):
    project_db = project_service.handle_get_all_data_service(db=db)
    return project_db

# Create : 
# Tạo dự án theo ID người dùng 
# Tạo dự án băng role admin 

@router.post("/",status_code=status.HTTP_201_CREATED ,response_model=ProjectSchema.ProjectResponse)
async def create_project(payload : ProjectSchema.ProjectCreateRequest ,db: Session = Depends(handle_connect_DB)):
    new_project_db = project_service.handle_create_project_service(payload=payload,db=db)
    if not new_project_db : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Không tìm thầy người dùng")
    return new_project_db

# Update : (PUT và Patch)
# Cập nhật dự án theo ID người dùng 
# Cập Nhật dự án băng role admin

@router.put("/{project_id}",status_code=status.HTTP_200_OK ,response_model=ProjectSchema.ProjectResponse)
async def update_project(project_id : int , payload : ProjectSchema.ProjectUpdateRequest ,db: Session = Depends(handle_connect_DB)):
    update_project_db = project_service.handle_update_project_service(payload=payload,db=db, project_id=project_id)
    # if not new_project_db : 
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Không tìm thầy người dùng")
    return update_project_db

# Delete : 
# Xóa dự án theo ID người dùng , và phải truyền thêm ID dự án
# Xóa toàn bộ dự án của người dùng muốn xóa 


@router.delete("/{project_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_project(project_id : int ,db: Session = Depends(handle_connect_DB)):
    delete_project_db = project_service.handle_delete_project_service(db=db, project_id=project_id)
    # if not new_project_db : 
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Không tìm thầy người dùng")
    return delete_project_db