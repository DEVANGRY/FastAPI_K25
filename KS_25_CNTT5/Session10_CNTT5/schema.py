# Thực thể users , products
from database import Base
from sqlalchemy import Column , Integer , String , Boolean , DateTime
from sqlalchemy.sql import func

class UsersSchema(Base) :
    # Tên thực thể Table : từ database
    __tablename__ = "users"

    id = Column(Integer , autoincrement=True , primary_key=True , index=True)
    name_user = Column(String(100) , nullable=False)
    email = Column(String(100) , nullable=False , unique=True)
    is_active = Column(Boolean , default=True)
    create_at = Column(DateTime , server_default=func.now())