from database import Base 
from sqlalchemy import Column , String , Integer
from sqlalchemy.orm import relationship
class CourseModel (Base):
    __tablename__ = "course" 
    id = Column(Integer , primary_key=True)
    name_course = Column(String(50) , nullable=False)
    detail_course = Column(String(50) , nullable=False)

    students = relationship("EmployeesModel",secondary="enrollment_table" , back_populates="courses")