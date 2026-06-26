from fastapi import FastAPI

app = FastAPI(
    title="Web nhận định tỉ lệ bóng WC",
    description="Hệ Thống sẽ xây dựng các API để tính toán siêu kết quả để làm giàu dễ hơn",
    contact= {
        "name" : "Tùng Other",
        "email" : "tungbebong@gmail.com",
    },
    version="1.0.0"
)

@app.get("/dashboard/{id}", tags=["Dashboard"])
def get_data(id:str):
    # Xử lý logic
    return {"message" :"Xin chào Chương Trình FASTAPI đầu tiên" , "id" : f"{id}"}