from pydantic import BaseModel , ConfigDict

class CreateBookRequest(BaseModel):
    title : str 
    author : str
    category : str

class BookResponse(BaseModel):
    id : int
    title : str 
    author : str
    category : str

    model_config = ConfigDict(from_attributes=True)

class GetAllBookResponse(BaseModel):
    message : str 
    data : list[BookResponse]