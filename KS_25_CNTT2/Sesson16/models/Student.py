from database import Base 
from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import relationship

class StudentModel(Base) :
    __tablename__ = "student"

    id = Column(Integer , primary_key=True , autoincrement=True , index= True)
    full_name = Column(String(30) , nullable=False)
    status = Column(String(30) ,default="ACTIVE") 
    department_id = Column(Integer , ForeignKey("department.id"),nullable=False)

    department = relationship("DepartmentModel",back_populates="students")

    courses= relationship("CourseModel",secondary="enrollment",back_populates="students")


    