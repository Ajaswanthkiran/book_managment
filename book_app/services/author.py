
from book_app.db.models.author import Author

def get_all_authors(session):
    try:
        return session.query(Author).all()
    except Exception as e:
        return False
    
def get_by_id(id,session):
    try:
        res=session.query(Author).filter(Author.id==id).first()
        return res
    except Exception as e:
        return False
    




def isUserPresent(user_name,session):
    res=session.query(Author).filter(Author.user_nam==user_name).all()
    if res is None:
        return True
    return False

def add(author,session):
    try:
        session.add(author)
        session.commit()
        return True
    except Exception as e:
        return False

def update_author(id,author_details,session):
    try:
        res=session.query(Author).get(id)
        res.name=author_details.name
        res.password=author_details.password
        res.mail=author_details.mail
        session.commit()
        return True
    except Exception as e:
        return False


def delete(id,session):
    try:
        res=session.query(Author).get(id)
        session.delete(res)
        session.commit()
        return True
    except Exception as e:
        return False
