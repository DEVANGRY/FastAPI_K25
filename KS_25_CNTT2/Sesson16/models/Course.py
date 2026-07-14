from database import Base 
from sqlalchemy import Column , Integer , String 
from sqlalchemy.orm import relationship

class CourseModel(Base) :
    __tablename__ = "course"

    id = Column(Integer , primary_key=True , autoincrement=True , index= True)
    name = Column(String(30) , nullable=False , unique=True)
    status = Column(String(30) , default="OPEN")

    students = relationship("StudentModel" , secondary="enrollment" , back_populates="courses")