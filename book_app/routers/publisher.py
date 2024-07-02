
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from book_app.db.database import get_db

from  fastapi_pagination import paginate,Page,Params
from book_app.routers import oauth2
from book_app.schemas.token import TokenData
from book_app.services import publisher as crud
from book_app.schemas.publisher import Publisher,PublisherOut 
from book_app.db.models.publisher import Publisher as PUBLISHER

from book_app.services.hassing import Hash 


router=APIRouter(prefix="/publisher",
                 tags=['Publisher']
)

@router.get("/list",response_model=list[PublisherOut])
def get_all(db: Session=Depends(get_db),get_current_user: TokenData=Depends(oauth2.get_current_active_publisher)):
    return crud.get_all(db)


@router.post("")
def insert(publisher: Publisher,db: Session=Depends(get_db),get_current_user: TokenData=Depends(oauth2.get_current_active_publisher)):
    
    hash=Hash()
       
    res=PUBLISHER(name=publisher.name,password=hash.bcrypt(publisher.password))
        
    return crud.insert(res,db)
    

@router.put("/{id}")
def update_by_id(id: int,name: str,db: Session=Depends(get_db),get_current_user: TokenData=Depends(oauth2.get_current_active_publisher)):
    return crud.update(id,name,db)


@router.delete("/{id}")
def delete(id:int,db: Session=Depends(get_db),get_current_user: TokenData=Depends(oauth2.get_current_active_publisher)):
    return crud.delete(id,db)

@router.get("/page",response_model=Page[PublisherOut])
def get_page(param: Params=Depends(), db: Session=Depends(get_db),get_current_user: TokenData=Depends(oauth2.get_current_active_publisher)):
    res=crud.get_all(db)


@router.get("/{id}",response_model=PublisherOut | bool)
def get_publisher_by_id(id:int,db: Session=Depends(get_db),get_current_user: TokenData=Depends(oauth2.get_current_active_publisher)):
    return crud.get_publisher_by_id(id,db)
    return paginate(res,param)