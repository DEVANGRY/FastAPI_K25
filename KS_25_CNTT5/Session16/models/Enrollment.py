# Xây dựng bảng trung gian 
from sqlalchemy import Column , Integer , ForeignKey
from database import Base
# Cách 1 : 
# enrollment_model = Table(
#     "enrollment",
#     Base.metadata, 
#     Column("user_id",Integer ,ForeignKey("user.id")),
#     Column("course_id",Integer ,ForeignKey("course.id"))
# )

# Cách 2 : tạo model 
class EnrollmentModel(Base) :
    __tablename__ = "enrollment"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer ,ForeignKey("user.id"))
    course_id = Column(Integer ,ForeignKey("course.id"))