from fastapi import FastAPI

app = FastAPI(
    title="Đây là Chương Trình FastAPI đầu tiên của CNTT1",
    description="Đây dùng để tạo API Hello world",
    version="1.0.0",
    contact={
        "name": "Dev",
        "email": "@gmail.com"
    }
)

# Endpoint API đầu tiên : in ra chữ Hello world
@app.get("/dashboard",tags=["Dashboard"])
def get_data():
    """Đây là API để khởi động dự án"""
    return {"message" : "Đây là dữ liệu của trang dashboard"}

@app.get("/dashboard2",tags=["Auth"])
def get_data():
    # code code 
    return {"message" : "Đây là dữ liệu của trang dashboard"}