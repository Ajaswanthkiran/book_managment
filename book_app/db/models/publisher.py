

from sqlalchemy import Column,Integer,String,UUID

from sqlalchemy.orm import relationship

from book_app.db.database import Base


class Publisher(Base):

    __tablename__="publisher"
    
    __table_args__ ={"schema":"sample"}
    #pk_publisher_
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String,nullable=False,unique=True)
    

