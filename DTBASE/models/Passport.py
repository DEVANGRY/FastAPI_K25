from database import Base
from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import relationship

class PassportModel (Base) :
    __tablename__ = "passport"

    id = Column(Integer , primary_key=True)
    passport_card_number = Column(String(15) , unique=True , nullable= False )
    address = Column(String(100), nullable=False)

    employee_id = Column(Integer, ForeignKey("employee.id"), unique=True)

    owner = relationship("EmployeesModel", back_populates="passport")