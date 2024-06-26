
from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from book_app.db.database import get_db
from book_app.services import author


router=APIRouter(
    prefix="/author"
)


@router.get("")
def get_all_authors(db: Session=Depends(get_db)):
    return author.get_all_authors(db)