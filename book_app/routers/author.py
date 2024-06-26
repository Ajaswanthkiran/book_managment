
from fastapi import APIRouter,Depends

from ..db.database import Session
from sqlalchemy.orm import Session


from ..services import author
route=APIRouter(
    prefix="/author"
)


def get_db():
    session=Session()
    try:
        yield session
    finally:
        session.close()


@route.get("")
def get_all_authors(db: Session=Depends(get_db)):
    return author.get_all_authors(db)