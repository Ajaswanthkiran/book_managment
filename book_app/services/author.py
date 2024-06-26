
from ..db.models.author import Author


def get_all_authors(session):
    return session.query(Author).all()

def get_by_id(id,session):
    res=session.query(Author).filter(Author.id==id).first()
    return res

def add(author,session):
    session.add(author)
    session.commit()
    return "added"

def update_author(author_details,session):
    res=session.query(Author).filter(Author.user_name==author_details.user_name).first()
    res[0].name=author_details.name
    res[0].password=author_details.password
    res[0].mail=author_details.mail
    return res