from database import Base 
from sqlalchemy import Column, Integer , String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class UserModel (Base):
    __tablename__ = "user"

    id = Column(Integer,primary_key=True)
    username = Column(String(25) , unique=True , nullable=False)
    password = Column(String(50) , nullable=False )
    is_activate = Column(Boolean , nullable=False)

    role_id = Column(Integer , ForeignKey("role.id") )

    role = relationship("RoleModel",back_populates="users")
