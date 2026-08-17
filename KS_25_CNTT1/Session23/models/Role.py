from database import Base 
from sqlalchemy import Column, Integer , String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class RoleModel (Base):
    __tablename__ = "role"

    id = Column(Integer,primary_key=True)
    role_name = Column(String(25) , unique=True , nullable=False)
    det = Column(String(255))

    users = relationship("UserModel",back_populates="role")


    