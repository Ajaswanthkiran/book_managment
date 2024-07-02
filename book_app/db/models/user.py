
from sqlalchemy import Column,Integer,String,UUID

from sqlalchemy.orm import relationship

from book_app.db.database import Base


class User(Base):

    __tablename__="user"
    
    __table_args__ ={"schema":"sample"}
    # pk_user_
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String,nullable=False,)
    user_name=Column(String,nullable=False,index=True,unique=True)
    password=Column(String,nullable=False)
    mail=Column(String,nullable=False,unique=True)
    role=Column(String, default="user")
    

