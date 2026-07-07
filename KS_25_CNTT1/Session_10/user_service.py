from sqlalchemy.orm import Session
from schema import CreateUserRequest
from models import UserModel

def handle_create_user_service ( user_new : CreateUserRequest , db : Session) :
    create_data_user_database = UserModel(
        name_user = user_new.name_user,
        phone = user_new.phone,
        email = user_new.email,
        is_active = user_new.is_active
    )

    # Bước tiếp theo : Thêm vào DB 
    db.add(create_data_user_database)

    # Đẩy dữ liệu vào DB
    db.commit()

    # Load lại dữ liệu 
    db.refresh(create_data_user_database)

    return create_data_user_database

def handle_get_all_data(db: Session):
    return db.query(UserModel).all()