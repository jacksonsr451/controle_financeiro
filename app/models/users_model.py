from app.ext.flask_sqlalchemy import db
from werkzeug.security import generate_password_hash, check_password_hash



class UsersModel(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    
    
    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        
    
    @staticmethod
    def verify_password(passowrd):
        return check_password_hash(UsersModel.password,passowrd)
    
    
    @staticmethod
    def add(request) -> bool:
        try:
            user = UsersModel(username=request["username"], password=request["password"], email=request["email"])
            db.session.add(user)
            db.session.commit()
            return True
        except:
            return False
        
    
    @staticmethod
    def all():
        return UsersModel.query.all()
    
    
    @staticmethod
    def delete(id) -> bool:
        user = UsersModel.query.get(id)
        if user is not None:
            db.session.delete(user)
            db.session.commit()
            return True
        else:
            return False
        