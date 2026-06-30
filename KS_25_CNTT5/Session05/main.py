from fastapi import FastAPI , HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel , Field

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Cho phép tất cả domain gọi vào
    allow_credentials=False,      # Nếu không dùng cookie/session thì để False
    allow_methods=["*"],          # Cho phép GET, POST, PUT, DELETE, PATCH...
    allow_headers=["*"],          # Cho phép mọi header, gồm Content-Type, Authorization...
)


# App Quản lý Công Việc Của HuanDz
list_todo = [
    {"id" : 1 , "name" : "Tán gái" , "status" : False , "time_todo" : 20},
    {"id" : 2 , "name" : "Soi kèo bóng banh" , "status" : True , "time_todo" : 180},
    {"id" : 3 , "name" : "Chơi Game Công Chúa" , "status" : False , "time_todo" : 60},
    {"id" : 4 , "name" : "Chơi Tài Cỉu" , "status" : True , "time_todo" : 5},
]

# Xây dựng project API quản lý todolist 
# API 1 : Lấy toán bộ dự liệu từ database
# 2: Lấy công việc dựa vào ID 
# 3: Thêm công việc vào database
# 4 : Sửa thông tin công việc 
# 5 : Xóa công việc 
# 6 : Tìm kiếm công việc dựa vào tên
# 7 : tìm kiếm công việc dựa vào trạng thái hoàn thành 

# API 1 : Lấy toán bộ dự liệu từ database : GET
@app.get("/todos",tags=["Todos"])
def get_list_todo ():
    """Đây là API lấy toàn bộ dữ liệu công việc"""
    return {"message" : "Lấy dữ liệu danh sách thành công" , "data" : list_todo}

# 2: Lấy công việc dựa vào ID : GET
@app.get("/todos/{todo_id}",tags=["Todos"])
def get_todo_detail(todo_id : int):
    """Đây là API lấy công việc cụ thể"""
    print(list_todo)
    for todo in list_todo:
        if todo["id"] == todo_id:
            return {"message" :f"Lấy được công việc có ID = {todo_id} thành công" , "data" : todo}
    
    raise HTTPException(status_code=404,detail="Không tim thấy ID mong muôn")


class TodoCreate(BaseModel):
    id : int | None = None
    name : str =  Field(...,min_length=0 , max_length=30)
    status : bool =Field(default=False,description="Đây là trường dùng để miêu tả trạng thái")
    time_todo : int = Field(...,gt=0 , lt=10000)

# 3: Thêm công việc vào database:   POST
@app.post("/todos",tags=["Todos"])
def create_todo(new_todo : TodoCreate):
    list_todo.append(new_todo.model_dump())
    return {"message" : "Đã thêm công việc thành công" , "data" : new_todo}

# 4: Sửa công việc vào database:   PUT OR Path
@app.put("/todos/{todo_id}",tags=["Todos"])
def update_todo(todo_id : int , new_todo : TodoCreate):
    for todo in list_todo:
        if todo["id"] == todo_id :
            todo.update(new_todo.model_dump())
            return {"message" : "Sửa thành công"}
        
    raise HTTPException(status_code=404 , detail="Không tìm thấy ID muốn sửa")

# 4: Xóa công việc vào database:   DELETE
@app.delete("/todos/{todo_id}",tags=["Todos"])
def delete_todo(todo_id : int):
    for todo in list_todo:
        if todo["id"] == todo_id :
            list_todo.remove(todo)
            return {"message" : "Đã xóa thành công" }
    raise HTTPException(status_code=404 , detail="Không tìm thấy ID muốn sửa")
