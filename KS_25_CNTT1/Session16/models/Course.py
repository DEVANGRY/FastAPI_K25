from database import Base
from sqlalchemy import Column , String , Integer , ForeignKey
from sqlalchemy.orm import relationship

class CourseModel(Base) :
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String(50), nullable=False)
    course_detail  = Column(String(12), nullable=False)
    money = Column(Integer, nullable=False)
    status = Column(String(15), default="OPEN")


    # Bước tạo liện kết với bảng Course
    users = relationship("UserModel",secondary="enrollment",back_populates="courses")
