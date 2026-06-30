from fastapi import FastAPI, HTTPException
from pydantic import BaseModel , Field

# Làm một Project API để quản lý list công việc hàng ngày 
list_todo_do = [
    {"id" : 0 , "name_todo" : "Chơi Game" , "status" : True , "time_todo" : 600},
    {"id" : 1 , "name_todo" : "Xem Phim" , "status" : False , "time_todo" : 120},
    {"id" : 2 , "name_todo" : "Đi chơi với NY" , "status" : False , "time_todo" : 0},
    {"id" : 3 , "name_todo" : "Ăn" , "status" : False , "time_todo" : 2},
    {"id" : 4 , "name_todo" : "Xem TopTop" , "status" : False , "time_todo" : 1000},
]

# Xây dựng các API để quản lý danh sách này 
# API : 
# 1.Xem danh sách công việc : GET
# 2.Thêm Công việc 
# 3.Cập Nhật Thông tin Công Việc 
# 4.Xóa Công Việc 
# 5.Tìm Kiếm công việc theo ID 
# 6.Lọc công việc theo trạng thái hoàn thành 

app = FastAPI()

# 1.Xem danh sách công việc : GET
@app.get("/todos",tags=["Todos"] , status_code= 200)
async def get_all_data():
    """Đây là API dùng để lấy toàn bộ dữ liệu từ DATABASE"""
    return {"message" : "Lấy dữ liệu công việc thành công" , "data" : list_todo_do , "status_code" : 200}

# 2.Xem chi tiết công việc theo ID : GET
@app.get("/todos/{todo_id}", tags=["Todos"] , status_code=200)
async def get_todo_detail (todo_id :int):
    for todo in list_todo_do:
        if todo["id"] == todo_id:
            return {"message" : "Lấy công việc theo ID thành công" , "data" : todo}
    raise HTTPException(status_code=404 , detail=f"Không tìm thấy công việc có ID = {todo_id}")

class TodoCreate(BaseModel):
    id : int
    name : str = Field(...,min_length=2)
    status : bool = Field(default=False)
    time_todo : int = Field(gt=0)

# 3.Thêm Công việc : POST
@app.post("/todos",tags=["Todos"])
async def create_todo(new_todo : TodoCreate):
    list_todo_do.append(new_todo)
    return {"message" : "Thêm công việc thành công" , "data" : new_todo}

# 4.Cập Nhật Thông tin Công Việc : 
@app.put("/todos/{todo_id}",tags=["Todos"])
async def update_todo (todo_id:int , todo_update : TodoCreate):
    for todo in list_todo_do:
        if todo["id"] == todo_id:
            todo.update(todo_update)
            return {"message" : "Update công việc thành công" , "data" : todo}
    raise HTTPException(status_code=404 , detail= f"Không tìm thấy Công việc có ID = {todo_id}")

# 5.Xóa Công Việc : delete

@app.delete("/todos/{todo_id}",tags=["Todos"])
async def delete_todo(todo_id : int):
    for todo in list_todo_do:
        if todo["id"] == todo_id:
            list_todo_do.remove(todo)
            return {"message" : "Xóa công việc thành công"} 
    raise HTTPException(status_code=404 , detail= f"Không tìm thấy Công việc có ID = {todo_id}")
    