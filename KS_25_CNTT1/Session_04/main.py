from fastapi import FastAPI, Path , Query
from pydantic import BaseModel , Field

app = FastAPI()

list_student = [
    {"id" : 1 , "name" : "Dev" , "age" : 19 },
    {"id" : 2 , "name" : "Sơn" , "age" : 20 },
    {"id" : 3 , "name" : "An" , "age" : 18 },
    {"id" : 4 , "name" : "Thuy" , "age" : 21 },
]

# Xây dựng các endpoint 
# Xây dựng một API để lấy toàn bộ dữ liệu của sinh viên có ID là 1
@app.get("/students/detail_student/{student_id}",tags=["Students"])
async def get_detail_student (student_id : int = Path(...,gt=10)):
    for student in list_student:
        if student["id"] == student_id:
            return {"message" : "Lấy dữ liệu của sinh viên thành công " , "data" : student}
    return {"message" : f"Không có dữ liệu của sinh viên có ID là {student_id}"}


# @app.get("/students/detail_student/2")
# @app.get("/students/detail_student/3")

# Tạo cho tôi một API dùng để lọc các sinh viên có tuổi lớn hơn 18 nhỏ hơn 20 giới tính nữ 
@app.get("/students/filter" , tags=["Students"])
async def handle_filter_student_by_age (tuoi_nho_hon : int = Query(default=18), tuoi_lon_hon : int = Query()):
    new_list_filter = []
    for student in list_student:
        if tuoi_nho_hon <= student["age"] <= tuoi_lon_hon:
            new_list_filter.append(student)
    return {"message" :"Lấy dữ liệu tìm kiếm thành công" , "data" : new_list_filter}

class StudentCreate (BaseModel): 
    id : int = Field(...,gt=0,lt=100,description="Đây là trường ID của sinh viên")
    name : str 
    age : int  = Field(default=19)

# Xây dựng một API dùng để Thêm sinh viên vào trong Database (list_student)
@app.post("/students",tags=["Students"])
async def create_student(newStudent : StudentCreate):
    list_student.append(newStudent)
    return {"message" : "Thêm sinh viên thành công" , "data" : list_student}