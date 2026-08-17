from database import Base 
from sqlalchemy import Column , String , Integer
from sqlalchemy.orm import relationship

class RoleModel(Base) :
    __tablename__ = "role"

    id = Column(Integer , primary_key=True , autoincrement=True) 
    role_name = Column(String(50) , unique=True)

    users = relationship("UserModel" , back_populates="role")