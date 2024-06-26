
from fastapi import APIRouter,Depends

from ..services import book
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
    return book.get_all_book(db)

    
@router.get("/books/{id}")
def get_book_by_id(id:int,db: Session=Depends(get_db)):
    return book.get_book_by_id(id,db)

@router.post("/books")
def add_book(b:book.Book,db: Session=Depends(get_db)):
    details=Book(title=b.title,author=b.author,publication_data=b.publication_date,isbn=b.isbn)
    return book.add_book(details,db)


@router.put("/books/{book_id}")
def update__book_title_by_author_name(id:int,updated_details:book.Book,db: Session=Depends(get_db)):
    return book.update_book_title(id,updated_details,db)


@router.delete("/book/{id}")
def delete(id:int,db:Session=Depends(get_db)):
    return book.delete_book(id,db)