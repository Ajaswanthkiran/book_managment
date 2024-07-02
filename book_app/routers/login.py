

from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from book_app.db.database import get_db

from book_app.schemas.login import Login

from book_app.db.models import user

from fastapi.security import OAuth2PasswordRequestForm

from book_app.services import login as c, token
router=APIRouter(
    prefix="/login",
    tags=["Login"]
)


@router.post("")
def login(details: OAuth2PasswordRequestForm= Depends(),db: Session=Depends(get_db)):
    res=c.check(details.username,details.password,db)
    if not res:
        return False
    
    if res.role!="publisher":
        access_token = token.create_access_token(
            data={"sub": res.user_name,'role':res.role})
        return {"access_token":access_token, "token_type":"bearer"}
    access_token = token.create_access_token(
            data={"sub": res.username,'role':res.role})
    return {"access_token":access_token, "token_type":"bearer"}