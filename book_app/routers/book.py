
from fastapi import APIRouter,Depends

from fastapi.responses import FileResponse

from book_app.services import book as crud
from book_app.db import database
from book_app.db.models.book import Book
from book_app.schemas import book

from fastapi_pagination import paginate,Page,Params
from book_app.db.database import get_db

from book_app.routers import oauth2
from book_app.schemas.token import TokenData

from sqlalchemy.orm import Session

router=APIRouter(tags=['Books']
)


@router.get("/books/list",response_model=list[book.BookOut])
def get_all_books(db: Session=Depends(get_db)):
    return crud.get_all_book(db)

@router.get("/books/page", response_model=Page[book.BookOut])
def get_book_page(page:int,size:int,db: Session=Depends(get_db)):
    param=Params(page=page,size=size)
    res=crud.get_all_book(db)
    return paginate(res,param)
    
@router.get("/books/{id}",response_model=book.BookOut)
def get_book_by_id(id:int,db: Session=Depends(get_db)):
    return crud.get_book_by_id(id,db)

@router.post("/books")
def add_book(b:book.Book,db: Session=Depends(get_db)):
    details=Book(title=b.title,author_user_name=b.author_user_name,publisher_name=b.publisher_name,publication_date=b.publication_date,isbn=b.isbn)
    return crud.add_book(details,db)
    

@router.put("/books/{id}")
def update__book_title_by_id(id:int,updated_details:book.UpdateBook,db: Session=Depends(get_db)):
    return crud.update_book_title(id,updated_details,db)


@router.delete("/book/{id}")
def delete(id:int,db:Session=Depends(get_db)):
    return crud.delete_book(id,db)

   

@router.get("/book/weeklyreport" )
def get_weeklyreport():

    # return FileResponse(path=r"C:\Users\16307\Desktop\book_managment\weekly_report.csv",filename="weekly_book_report.csv",media_type="csv")
    return FileResponse(path=r"C:\Users\16307\Desktop\book_managment\weekly_report.csv", filename="weekly_book_report.csv", media_type='application/octet-stream', headers={"Content-Disposition": "attachment; filename=sample.csv"})
