from database import Base 
from sqlalchemy import Column , Integer , String , Boolean , DateTime
from sqlalchemy.sql import func

class UserModel(Base):
    # Tên của bảng , thực thể nằm trong database
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_user = Column(String(100) , nullable=False , index=True)
    phone = Column(String(100) , nullable=False , index=True , unique=True)
    email = Column(String(100) , nullable=False , index=True , unique=True)
    is_active = Column(Boolean , default=True)
    create_at = Column(DateTime , server_default=func.now())

