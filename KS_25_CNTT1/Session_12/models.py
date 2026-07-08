# Chứa tất các bảng trong DATABASE 
import database
from sqlalchemy import Column,Integer,String , Boolean , DateTime
from sqlalchemy.sql import func

class AccountUserModel(database.Base):
    # Tên Bảng Trong Database
    __tablename__ = "account_users"

    # Các thuộc tính , cột của bảng 

    id = Column(Integer , primary_key=True , autoincrement=True)
    account = Column(String(25) , nullable=False, unique=True)
    password = Column(String(30) ,nullable=False)
    email = Column(String(35) , nullable=False, unique=True)
    is_active = Column(Boolean ,default=True)
    create_at = Column(DateTime , server_default=func.now())