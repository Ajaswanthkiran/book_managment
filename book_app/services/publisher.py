
from book_app.db.models.publisher import Publisher 

def get_all(session):
    return session.query(Publisher).all()


def insert(p,session):
    session.add(p)
    session.commit()
    return 'added'

def update(id,name,session):
    res=session.query(Publisher).filter(Publisher.id==id).first()
    res[0].name=name
    return "updated"

