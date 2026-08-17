from database import Base 
from sqlalchemy import Column , Integer , String, ForeignKey
from sqlalchemy.orm import relationship

class UserModel(Base) :
    __tablename__ = "user"

    id = Column(Integer , primary_key=True , autoincrement=True)
    username = Column(String(50) , unique=True , nullable=False)
    password = Column(String(100), nullable=False)
    role_id = Column(Integer ,ForeignKey("role.id"),nullable=False)

    role = relationship("RoleModel",back_populates="users")
