
from ..db.models.author import Author


def get_all_authors(session):
    session.query(Author).all()