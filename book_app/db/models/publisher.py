

from sqlalchemy import Column,Integer,String,UUID

from sqlalchemy.orm import relationship

from book_app.db.database import Base


class Publisher(Base):

    __tablename__="publisher"
    
    #pk_publisher_
    id=Column(UUID,primary_key=True)
    name=Column(String,nullable=False,unique=True)
    

