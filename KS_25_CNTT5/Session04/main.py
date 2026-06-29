from fastapi import FastAPI, HTTPException,Query
from pydantic import BaseModel , Field

app = FastAPI()

list_user_data = [
    {"id" : 1 , "name" : "Hoàng Văn" , "phone" : "03635789999" , "age" : 18},
    {"id" : 2 , "name" : "Dev 123" , "phone" : "0312345677" , "age" : 19},
    {"id" : 3 , "name" : "Hoàng Văn V2" , "phone" : "012345678" , "age" : 20},
    {"id" : 4 , "name" : "Hoàng Văn V4" , "phone" : "0000000000" , "age" : 18},
    {"id" : 4 , "name" : "Hoàng Văn V4" , "phone" : "0000000000","age" : 18},
]

@app.get("/")
async def get_data():
    return {"message" : "Đây là dữ liệu trang chủ"}

# Tạo một api để lấy dữ liệu của sinh viên đầu tiên 
@app.get("/student/0")
async def get_data_first_student():
    return list_user_data[0]

# Tạo một api để lấy dữ liệu của sinh viên đầu tiên 
@app.get("/student/1")
async def get_data_first_student():
    return list_user_data[1]

# path 
@app.get("/students/{student_id}")
async def get_data_detail_student(student_id : int):
    student_find = None
    for student in list_user_data:
        if student["id"] == student_id:
            student_find = student
    if student_find is None :
        raise HTTPException(status_code=404 ,detail= "Không tìm thầy Sinh viên nào có ID như vậy")
    else :
        return {"message" : "Lấy thông tin sinh viên" , "data" : student_find}

# Filter lấy những sinh viên có tuổi nhỏ hơn 19 
@app.get("/filter_by_age")
async def filter_student_by_age (age_student : int = Query(...,gt=0 ,lt=20),name_student : str = Query()):
    list_student_filter = []
    for student in list_user_data:
        if student["age"] <= age_student:
            list_student_filter.append(student)
    return {"message" : "Danh sách sinh viên cần tìm kiếm thành công" , "data" : list_student_filter}

class studentDTO(BaseModel) :
    id : int = Field(gt=0 , lt=100)
    name: str
    phone : str
    age : str

# Api để thêm sinh viên 
@app.post("/students")
async def create_student(student : studentDTO):
    list_user_data.append(student)
    return {"message" : "Thêm sinh viên thành công"}