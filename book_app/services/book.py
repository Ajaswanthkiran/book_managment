

from book_app.db.models.book import Book

def get_all_book(session):
    return session.query(Book).all()


def get_book_by_id(id,session):
    return session.query(Book).filter(Book.id==id).first()
    

def add_book(details,session):
    session.add(details)
    session.commit()
    return "Book added successfully"


def update_book_title(id,details,session):
    res=session.query(Book).filter(Book.id==id).first()
    res.title=details.title
    res.author=details.author
    res.isbn=details.isbn
    res.publication_date=details.publication_date

    session.commit()
    return "Updated Successfully"
    
def delete_book(id,session):
    res= session.query(Book).get(id)
    session.delete(res)
    session.commit()
    return "Book deleted successfully"