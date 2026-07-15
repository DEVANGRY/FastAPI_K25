from sqlalchemy.orm import Session , joinedload
from models import ProjectModel, UserModel
from schemals import project_schemal


def handle_get_all_data_project (db : Session):
    projects_db = db.query(ProjectModel).options(joinedload(ProjectModel.user)).all()
    return projects_db

def handle_create_project (payload : project_schemal.CreateProjectRequest,db : Session):
    # Kiểm tra user có tồn tại hay không 
    find_user_db = db.query(UserModel).filter(UserModel.id == payload.user_id).first()

    if not find_user_db:
        return None 
    
    create_project_db =  ProjectModel(
        project_name = payload.project_name,
        technology = payload.technology,
        day = payload.day,
        project_detail = payload.project_detail,
        user_id = payload.user_id,
    )
    db.add(create_project_db)
    db.commit()
    db.refresh(create_project_db)
    return create_project_db

def handle_delete_project (project_id : int , db : Session):
    delete_project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not delete_project:
        return False
    db.delete(delete_project)
    db.commit()
    return True


def handle_update_project (project_id: int , payload : project_schemal.CreateProjectRequest,db : Session):
    # Kiểm tra user có tồn tại hay không 
    find_user_db = db.query(UserModel).filter(UserModel.id == payload.user_id).first()

    if not find_user_db:
        return "NOT_FOUND_USER" 
    
    # Kiểm tra project có tồn tại hay không 
    find_project_db = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()

    if not find_project_db:
        return "NOT_FOUND_PROJECT"  

    new_update = payload.model_dump()
    for key , value in new_update.items():
        setattr(find_project_db,key,value)

    db.commit()
    db.refresh(find_project_db)
    return find_project_db