from database import Base
from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import Relationship
class PaymentModel (Base):
    __tablename__ = "payment"

    id = Column(Integer , primary_key=True)
    detail_payment = Column(String(200))
    type_payment = Column(String(25) , nullable=False)

    employee_id = Column(Integer , ForeignKey("employee.id"))
    employee = Relationship("EmployeesModel" , back_populates="payment")