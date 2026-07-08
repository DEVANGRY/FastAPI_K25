from sqlalchemy.orm import Session
from schema import CreateUserRequest , UpdateUserRequest
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


def handle_update_data_user(db: Session , user_id : int , user_update_data : UpdateUserRequest):
    user_db = db.query(UserModel).filter(UserModel.id == user_id).first()

    # Biến dữ liệu từ kiểu object về kiểu DICT 
    user_update_dict = user_update_data.model_dump(exclude_unset=True)

    if user_db :
        for key,value in user_update_dict.items():
            setattr(user_db , key ,value)
        db.commit()
        db.refresh(user_db)
    return user_db