from sqlalchemy.orm import Session , joinedload
from models import ProjectModel

def handle_get_all_data_project (db : Session):
    projects_db = db.query(ProjectModel).options(joinedload(ProjectModel.user)).all()
    return projects_db