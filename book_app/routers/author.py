
from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from book_app.db.database import get_db
from book_app.services import author as crud
from book_app.db.models.author import Author as author_insert
from fastapi_pagination import paginate,Page,Params
from book_app.schemas.author import Author,AuthorUpdate,AuthorOut


from book_app.routers import oauth2
from book_app.schemas.token import TokenData

from book_app.services.hassing import Hash 

router=APIRouter(
    prefix="/author",
    tags=['Author']
)





@router.get("/list",response_model=list[AuthorOut])
def get_all_authors(db: Session=Depends(get_db)):
    return crud.get_all_authors(db)

@router.get("/page",response_model=Page[AuthorOut])
def get_page(page:int,size:int, db: Session=Depends(get_db)):
    param=Params(page=page,size=size)
    res=crud.get_all_authors(db)
    print(res)
    return paginate(res,param)


@router.post("")
def insert_author(author: Author,db: Session=Depends(get_db)):
    hash=Hash()
    res=author_insert(name=author.name,user_name=author.user_name,password=hash.bcrypt(author.password),mail=author.mail)
    return  crud.add(res,db)
    

@router.put("/{id}")
def update_author(id:int,author: AuthorUpdate,db: Session=Depends(get_db)):
    return crud.update_author(id,author,db)


@router.delete("/{id}")
def delete_by_id(id:int,db: Session=Depends(get_db)):
    return crud.delete(id,db)


@router.get("/{id}",response_model=AuthorOut)
def get_by_id(id:int,db: Session=Depends(get_db)):
    return crud.get_by_id(id,db)
    