


from book_app.db.models.author import Author
from book_app.db.models.user import User
from book_app.db.models.publisher import Publisher
from .hassing import Hash

def check(username,password,session):
    user=session.query(User).filter(User.user_name==username).first()
    
    publisher=session.query(Publisher).filter(Publisher.name==username).first()
    author=session.query(Author).filter(Author.user_name==username).first()

    hash=Hash()
    
    if  user:
        if not hash.verify(password,user.password):
            return  False
    
        return user
    
    if publisher:
        if not hash.verify(password,publisher.password):
            return  False
    
        return publisher
    
    if author:
        if not hash.verify(password,author.password):
            return  False
    
        return author
    
    return False