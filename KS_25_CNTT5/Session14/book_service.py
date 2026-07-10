from sqlalchemy.orm import Session
from models import BooksModel
from sqlalchemy import asc,desc
def handle_get_all_data_service (db : Session):
    return db.query(BooksModel).all()

def handle_filter_book_by_title_service(title_book : str , db : Session):
    list_book_filter_db = db.query(BooksModel).filter(BooksModel.title.ilike(f"%{title_book}%")).all()
    return list_book_filter_db


def handle_sort_book_by_category(type_sort : str , db : Session):
    if (type_sort.upper() == "ASC") :
        # list_book_filter_db = db.query(BooksModel).order_by(BooksModel.category.asc()).all()

        list_book_filter_db = db.query(BooksModel).order_by(asc(BooksModel.category)).all()
    else :
        # list_book_filter_db = db.query(BooksModel).order_by(BooksModel.category.desc()).all()
        list_book_filter_db = db.query(BooksModel).order_by(desc(BooksModel.category)).all()

    return list_book_filter_db