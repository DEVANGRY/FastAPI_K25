from fastapi import FastAPI

app = FastAPI(
    title="Đây là API của CNTT2",
    description="Project này là dự án đầu tiên của CNTT2 K25",
    version="1.0.0",
    contact={
        "name" : "DevOps",
        "email" : "@gmail.com",
    }
)

@app.get("/home" , tags= ["Home Page"])
def get_data_home ():
    """Đây là API dùng để lấy toàn bộ dữ liệu"""
    return {"message" : "Đây là toàn bộ dữ liệu của trang chủ" , "status_code" : 200}

@app.get("/detail/{detail_id}", tags= ["Home Page"])
def get_data_home (detail_id:int):
    """Đây là API dùng để lấy Chi Tiết Dữ liệu"""
    # Code filter ....
    return {"message" : "Đây là dữ liệu chi tiết của sản phẩm" , "status_code" : 200, "id_detail" : detail_id}

@app.get("/contact", tags= ["Contact"])
def get_data_home ():
    """Đây là API dùng để lấy liên hệ của người dùng"""
    return {"message" : "Tôi là Minh Bé Bỏng" , "status_code" : 200 , "Phone" : "09999999"}