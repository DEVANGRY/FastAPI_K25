from database import Base
from sqlalchemy import Column , String , Integer , ForeignKey
from sqlalchemy.orm import relationship

class UserInfoModel(Base) :
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer , ForeignKey("user.id") , unique=True)
    sex = Column(String(12), nullable=False)
    address = Column(String(12), nullable=False)
    passport = Column(String(12), nullable=False)

    user = relationship("UserModel", back_populates="user_info")
