from sqlalchemy.orm import Session
# import models
from models import CreateUserRequest
from schema import UsersSchema

# Chứa toàn bộ logic làm việc giữa sqlalchemy và database

def create_user_service (db:Session , user_account : CreateUserRequest):
    db_user_create_new = UsersSchema(
        name_user = user_account.name_user,
        email = user_account.email,
        is_active = user_account.is_active,
    )
    # Thêm dữ liệu vào database
    db.add(db_user_create_new)

    # Phải thành công thì mới đẩy vào database
    db.commit()

    # Khi thêm thành công rồi thì sẽ lấy dữ liệu mới từ database đẩy lại db_user_create_new
    db.refresh(db_user_create_new)

    return db_user_create_new


def get_all_data_user (db:Session):
    return db.query(UsersSchema).all()