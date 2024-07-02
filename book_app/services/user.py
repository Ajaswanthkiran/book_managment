
from ..db.models.user import User


def get_all_users(session):
    try:
        return session.query(User).all()
    except :
        return False
    
def get_user_by_id(id,session):
    try:
        res=session.query(User).filter(User.id==id).first()
        return res
    except:
        return False

def add_user(user,session):
    try:    
        session.add(user)
        session.commit()
        return True
    except:
        return False

def update_user_by_id(id,user,session):
    try:
        res=session.query(User).get(id)
        res.name=user.name
        res.password=user.password
        res.mail=user.mail
        session.commit()
        return True
    except :
        return False


def delete(id,session):
    try:
        res=session.query(User).get(id)
        session.delete(res)
        session.commit()
        return True
    except:
        return False
