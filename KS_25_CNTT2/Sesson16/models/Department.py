from database import Base 
from sqlalchemy import Column , Integer , String 
from sqlalchemy.orm import relationship

class DepartmentModel(Base) :
    __tablename__ = "department"

    id = Column(Integer , primary_key=True , autoincrement=True , index= True)
    name = Column(String(30) , nullable=False , unique=True)

    # Nối với bảng Student 
    students = relationship("StudentModel",back_populates="department")