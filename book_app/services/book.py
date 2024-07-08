

from book_app.db.models.book import Book

from book_app.services.email_service import  sendmail

from book_app.db.models import author,publisher

def get_all_book(session):
    
    try:
        res=session.query(Book).all()
        return res
    except Exception as e:
        return e


def get_book_by_id(id,session):
    
    try:
        return session.query(Book).filter(Book.id==id).first()
    except :
        return False

def add_book(details,session):
    
    try:
        session.add(details)
        author_res=session.query(author.Author).filter(details.author_user_name==author.Author.user_name).first()
        
        print(author_res.mail)
        session.commit()

        sendmail(author_res.mail,details.title,details.author_user_name,details.publisher_name)
        # publisher_res=session.query(publisher.Publisher).filter(details.publisher_name).first()
        
        # sendmail(publisher_res.mail,details.title,details.author_user_name,details.publisher_name)
        
        return True
    except Exception as e:
        return e



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