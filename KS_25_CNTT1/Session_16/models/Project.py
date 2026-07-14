from database import Base
from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import relationship
# Tạo model dự án cá nhân 

class ProjectModel(Base):
    __tablename__ = "project"

    id = Column(Integer,primary_key=True , index=True)
    project_name = Column(String(50) , nullable=False , index=True)
    technology  = Column(String(70) , nullable=False , unique=True)
    day = Column(Integer)
    student_id = Column(Integer , ForeignKey("student.id"))
    # Tạo cầu nối đên bảng Student
    student = relationship("StudentModel",back_populates="projects")
