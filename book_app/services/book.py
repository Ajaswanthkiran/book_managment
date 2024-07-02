

from book_app.db.models.book import Book

def get_all_book(session):
    
    try:
        res=session.query(Book).all()
        return res
    except :
        return False


def get_book_by_id(id,session):
    
    try:
        return session.query(Book).filter(Book.id==id).first()
    except :
        return False

def add_book(details,session):
    
    try:
        session.add(details)
        session.commit()
        return True
    except :
        return False



def update_book_title(id,details,session):
    try:
        res=session.query(Book).filter(Book.id==id).first()
        res.title=details.title
        res.isbn=details.isbn
        res.publication_date=details.publication_date

        session.commit()
        return True
    except :
        return False
    
def delete_book(id,session):
    try:
        res= session.query(Book).get(id)
        session.delete(res)
        session.commit()
        return True
    except :
        return False