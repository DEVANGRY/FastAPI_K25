from database import Base 
from sqlalchemy import Column , Integer , String , Boolean , DateTime
from sqlalchemy.sql import func

class AccountUserModel(Base):
    __tablename__ = "account_user"

    # Thêm các cột trong database 
    id = Column(Integer , primary_key=True , autoincrement=True , index=True)
    username = Column(String(25) , nullable=False , unique=True)
    password = Column(String(30) , nullable=False )
    email =  Column(String(25) , nullable=False , unique=True)
    is_status = Column(Boolean , default=True) 
    create_at = Column(DateTime , server_default=func.now())