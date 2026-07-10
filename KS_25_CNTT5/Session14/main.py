from fastapi import FastAPI , Depends , status
import models
from database import Base , engine , handle_database 
from sqlalchemy.orm import Session
import book_service
from schemas import GetAllBookResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def check_api():
    return {"message" : "Chạy dự án thành công"}

# API thứ 2 : 
@app.get("/books" , status_code=status.HTTP_200_OK , response_model=GetAllBookResponse)
def get_all_book(db : Session = Depends(handle_database)):
    all_book_db = book_service.handle_get_all_data_service(db=db)

    return {"message" : "Lấy dữ liệu thành công" , "data" : all_book_db}

# API tìm kiếm 

@app.get("/books/search")
def filter_book_by_title(title_book : str , db : Session = Depends(handle_database)):
    list_book_filter = book_service.handle_filter_book_by_title_service(title_book=title_book, db=db)
    return {"message" : "Lấy dữ liệu thành công" , "data" : list_book_filter}


@app.get("/books/sort")
def sort_book_by_category(type_sort : str , db : Session = Depends(handle_database)):
    list_book_filter = book_service.handle_sort_by_category(type_sort=type_sort, db=db)
    return {"message" : "Lấy dữ liệu thành công" , "data" : list_book_filter}