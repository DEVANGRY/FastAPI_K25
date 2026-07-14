from database import Base
from sqlalchemy import Column , Integer , String
from sqlalchemy.orm import relationship
# Tạo model Sinh Viên 

class StudentModel(Base):
    __tablename__ = "student"

    id = Column(Integer,primary_key=True , index=True)
    name = Column(String(50) , nullable=False , index=True)
    email = Column(String(70) , nullable=False , unique=True)

    # Tạo cầu nối cho bảng student và studentinfo
    student_info = relationship("StudentInfoModel", back_populates="student" , uselist=False)

    # Tạo cầu nối đến bảng project 
    projects = relationship("ProjectModel" , back_populates="student")

    # Tạo cầu nối đên enrollment
    courses = relationship("CourseModel", secondary="enrollment" , back_populates="students")