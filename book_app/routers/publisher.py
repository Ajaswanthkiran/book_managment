
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from book_app.db.database import get_db

from book_app.services import publisher as crud
from book_app.schemas.publisher import Publisher 
from book_app.db.models.publisher import Publisher as PUBLISHER

router=APIRouter(prefix="/publisher")

@router.get("/list")
def get_all(db: Session=Depends(get_db)):
    return crud.get_all(db)

@router.post("")
def insert(publisher: Publisher,db: Session=Depends(get_db)):
    res=PUBLISHER(name=publisher.name)
    return crud.insert(res,db)
@router.put("/{id}")
def update_by_id(id: int,name: str,db: Session=Depends(get_db)):
    return crud.update(id,name,db)

