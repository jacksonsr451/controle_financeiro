from app.ext.flask_sqlalchemy import db
from werkzeug.security import generate_password_hash, check_password_hash



class UsersModel(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    despesas = db.relationship('DespesasModel', backref='users', lazy=True)
    receitas = db.relationship('ReceitasModel', backref='users', lazy=True)
    
    
    def __init__(self, username=None, email=None, password=None) -> None:
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        
    
    @staticmethod
    def verify_login(request) -> bool:
        user = UsersModel.query.filter_by(email=request["email"]).first()
        if not check_password_hash(user.password, request["password"]):
            return False
        return True
    
    
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
    
    
    @staticmethod
    def get(id):
        return UsersModel.query.get(id)
    
    
    @staticmethod
    def put(id, values) -> bool:
        try:
            data = UsersModel.get(id)
            data.username = values["username"]   
            data.email = values["email"]
            db.session.commit()
            return True
        except:
            return False
    