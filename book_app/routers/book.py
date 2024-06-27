
from fastapi import APIRouter,Depends

from ..services import book as crud
from ..db import database
from ..db.models.book import Book
from ..schemas import book



from sqlalchemy.orm import Session

router=APIRouter()

def get_db():
    session=database.Session()
    try:
        yield session
    finally:
        session.close()

    


@router.get("/books/list")
def get_all_books(db: Session=Depends(get_db)):
    return crud.get_all_book(db)

    
@router.get("/books/{id}")
def get_book_by_id(id:int,db: Session=Depends(get_db)):
    return crud.get_book_by_id(id,db)

@router.post("/books")
def add_book(b:book.Book,db: Session=Depends(get_db)):
    details=Book(title=b.title,author_user_name=b.author_user_name,publisher_name=b.publisher_name,publication_data=b.publication_date,isbn=b.isbn)
    return crud.add_book(details,db)


@router.put("/books/{id}")
def update__book_title_by_id(id:int,updated_details:book.UpdateBook,db: Session=Depends(get_db)):
    return crud.update_book_title(id,updated_details,db)


@router.delete("/book/{id}")
def delete(id:int,db:Session=Depends(get_db)):
    return crud.delete_book(id,db)