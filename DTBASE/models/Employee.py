from database import Base
from sqlalchemy import Column , Integer, String 
from sqlalchemy.orm import relationship


class EmployeesModel(Base) :
    __tablename__ = "employee"

    id = Column(Integer , primary_key=True)
    name = Column(String(50) , nullable=False )
    age = Column(Integer)

    passport = relationship("PassportModel" , back_populates="owner" , uselist=False)
    payment = relationship("PaymentModel" , back_populates="employee")
    courses = relationship("CourseModel" , secondary="enrollment_table", back_populates="students")