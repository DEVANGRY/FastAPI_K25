from database import Base
from sqlalchemy import Column , String , Integer , ForeignKey
from sqlalchemy.orm import relationship

class ProjectModel(Base) :
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String(50), nullable=False)
    technology = Column(String(12), nullable=False)
    day = Column(Integer, nullable=False)
    project_detail = Column(String(200), nullable=False)

    user_id = Column(Integer , ForeignKey("user.id"))

    # Bước tạo liện kết với bảng user
    user = relationship("UserModel",back_populates="projects")
    
