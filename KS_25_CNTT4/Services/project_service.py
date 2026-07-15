from sqlalchemy.orm import Session , joinedload
from models import ProjectModel , UserModel
import Schemals.Project as ProjectSchema

def handle_get_all_data_service (db : Session):
    projects_db = db.query(ProjectModel).options(joinedload(ProjectModel.user)).all()
    return projects_db

def handle_create_project_service(payload : ProjectSchema.ProjectCreateRequest ,db: Session):
    # Kiểm tra có tồn tại người dùng đó không
    is_user = db.query(UserModel).filter(UserModel.id == payload.user_id).first()

    if not is_user :
        return None

    new_project_db = ProjectModel(
        project_name = payload.project_name,
        technology = payload.technology,
        day = payload.day,
        project_detail = payload.project_detail,
        user_id = payload.user_id
    )
    db.add(new_project_db)
    db.commit()
    db.refresh(new_project_db)
    return new_project_db


def handle_update_project_service(project_id : int ,payload : ProjectSchema.ProjectUpdateRequest ,db: Session):
    # Kiểm tra có tồn tại người dùng đó không
    is_user = db.query(UserModel).filter(UserModel.id == payload.user_id).first()

    if not is_user :
        return "USER_NOT_FOUND"

    new_project_db = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not new_project_db :
        return "PROJECT_NOT_FOUND"

    update_project = payload.model_dump()
    for key , value in update_project.items():
        setattr(new_project_db , key , value)
    db.commit()
    db.refresh(new_project_db)

    return new_project_db


def handle_delete_project_service(project_id : int ,db: Session):
   
    delete_project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    db.delete(delete_project)
    db.commit()
    return True
