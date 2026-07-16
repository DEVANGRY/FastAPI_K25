from sqlalchemy.orm import Session , joinedload
from models import ProjectModel , UserModel
from Schemas import project_schema 

NOT_FOUND_PROJECT = "NOT_FOUND_PROJECT"
NOT_FOUND_USER = "NOT_FOUND_USER"

def handle_get_all_data_project_service (db : Session) : 
    project_all_db = db.query(ProjectModel).options(joinedload(ProjectModel.user)).all()
    return project_all_db

def handle_delete_project_by_id_service (project_id : int , db :Session):
    find_project_delete = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not find_project_delete :
        return NOT_FOUND_PROJECT
    db.delete(find_project_delete)
    db.commit()
    return True

def handle_create_project_service (payload : project_schema.ProjectRequest , db :Session):
    # Kiểm tra người dùng có tồn tại không 
    find_user_db = db.query(UserModel).filter(UserModel.id == payload.user_id).first()
    if not find_user_db :
        return NOT_FOUND_USER
    
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

def handle_update_project_service (project_id : int ,payload : project_schema.ProjectRequest ,db : Session):
    # Kiểm tra người dùng có tồn tại không 
    find_user_db = db.query(UserModel).filter(UserModel.id == payload.user_id).first()
    if not find_user_db :
        return NOT_FOUND_USER
    
    # Kiểm tra project có tồn tại không 
    find_project_db = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not find_project_db :
        return NOT_FOUND_PROJECT
    

    find_project_db.project_name = payload.project_name
    find_project_db.technology = payload.technology
    find_project_db.day = payload.day
    find_project_db.project_detail = payload.project_detail
    find_project_db.user_id = payload.user_id

    db.commit()
    db.refresh(find_project_db)
    return find_project_db
