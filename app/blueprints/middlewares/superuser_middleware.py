from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from app.models.users_model import UsersModel


def superuser_middleware(func):
    
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user = UsersModel.get_user_by_email(email=get_jwt_identity()["email"])
        if user.role == "Superuser":
            return func(*args, **kwargs)
        
        return jsonify({"message": "Precisa ser superuser para está rota!"})
    
    return decorated_function