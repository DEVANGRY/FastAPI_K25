from database import Base
from sqlalchemy import Column , Integer , String
from sqlalchemy.orm import relationship

# Tạo model khóa học
class CourseModel(Base):
    __tablename__ = "course"

    id = Column(Integer,primary_key=True , index=True)
    course_name = Column(String(50) , nullable=False , index=True)
    money = Column(Integer , nullable=False )
    status  = Column(String(70) , default="OPEN")

    # Tạo cầu nối đến enrollment
    students = relationship("StudentModel", secondary="enrollment" , back_populates="courses")
    