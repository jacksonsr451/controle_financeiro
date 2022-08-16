from datetime import timedelta
from flask_jwt_extended import create_access_token
from flask import jsonify, config
from flask_restful import Resource

from .....models.users_model import UsersModel

from ....requets.auth_request import AuthRequest



class Login(Resource):
    def get(self):
        pass
    
    
    def post(self):
        auth_request = AuthRequest.get()
        if UsersModel.verify_login(request=auth_request):
            token = create_access_token(identity={"email": auth_request["email"]}, expires_delta=timedelta(minutes=120))
            return jsonify({"token": token})
        return jsonify({"error": "Erro ao tentar login!"})
