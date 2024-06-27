
from ..db.models.user import User


def get_all_users(session):
    return session.query(User).all()

def get_user_by_id(id,session):
    res=session.query(User).filter(User.id==id).first()
    return res

def add_user(user,session):
    session.add(user)
    session.commit()
    return "added"

def update_user_by_id(id,user,session):
    res=session.query(User).get(id)
    res.name=user.name
    res.password=user.password
    res.mail=user.mail
    session.commit()
    return res


def delete(id,session):
    res=session.query(User).get(id)
    session.delete(res)
    session.commit()
    return "deleted"
