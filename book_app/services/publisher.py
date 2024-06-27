
from book_app.db.models.publisher import Publisher 

def get_all(session):
    return session.query(Publisher).all()

def get_publisher_by_id(id,session):
    res=session.query(Publisher).get(id)
    return res


def insert(p,session):
    session.add(p)
    session.commit()
    return 'added'

def update(id,name,session):
    res=session.query(Publisher).filter(Publisher.id==id).first()
    res[0].name=name
    return "updated"

def delete(id,session):
    res=session.query(Publisher).get(id)
    session.delete(res)
    session.commit()
    return "deleted"