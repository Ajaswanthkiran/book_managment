
from book_app.db.models.publisher import Publisher 

def get_all(session):
    try:
        return session.query(Publisher).all()
    except :
        return False

def get_publisher_by_id(id,session):
    try:
        res=session.query(Publisher).filter(Publisher.id==id).first()
        return res
    except :
        return False


def insert(p,session):
    
    try:
        session.add(p)

        session.commit()
        return True
    except :
        return False

def update(id,name,session):
    try:
        res=session.query(Publisher).get(id)
        res.name=name
        session.commit()
        return True
    except :
        return False

def delete(id,session):
    try:
        res=session.query(Publisher).get(id)
        session.delete(res)
        session.commit()
        return True
    except:
        return False