from database import Base
from sqlalchemy import Column , String , Integer 
from sqlalchemy.orm import relationship

class UserModel(Base) :
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    phone = Column(String(12), nullable=False , unique=True)
    age = Column(Integer, nullable=False)

    #  Bước tạo liên kết với bảng user_info 
    user_info = relationship("UserInfoModel", back_populates="user",uselist=False)

    # Bước tạo liện kết với bảng project 
    projects = relationship("ProjectModel",back_populates="user")

    # Bước tạo liện kết với bảng Course
    courses = relationship("CourseModel",secondary="enrollment",back_populates="users")
