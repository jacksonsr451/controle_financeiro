from app.ext.flask_sqlalchemy import db
from werkzeug.security import generate_password_hash, check_password_hash



class UsersModel(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    
    
    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        
    
    @staticmethod
    def verify_password(passowrd):
        return check_password_hash(UsersModel.password,passowrd)
