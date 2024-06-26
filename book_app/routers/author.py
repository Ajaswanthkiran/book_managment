
from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from book_app.db.database import get_db
from book_app.services import author as crud
from book_app.db.models.author import Author as author_insert

from book_app.schemas.author import Author,AuthorUpdate
router=APIRouter(
    prefix="/author"
)


@router.get("/list")
def get_all_authors(db: Session=Depends(get_db)):
    return crud.get_all_authors(db)

@router.get("/{id}")
def get_by_id(id:int,db: Session=Depends(get_db)):
    return crud.get_by_id(id,db)


@router.post("")
def insert_author(author: Author,db: Session=Depends(get_db)):
    res=author_insert(name=author.name,user_name=author.user_name,password=author.password,mail=author.mail)
    return  crud.add(res,db)
    

@router.put("")
def update_author(author: AuthorUpdate,db: Session=Depends(get_db)):
    return crud.update_author(author,db)