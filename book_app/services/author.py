
from ..db.models.author import Author


def get_all_authors(session):
    session.query(Author).all()


def add(author,db):
    db.add(author)
    db.commit()
    return "added"