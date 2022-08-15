from flask import jsonify
from flask_restful import Resource

from ....requets.users_request import UsersRequest

from .....models.users_model import UsersModel




class Users(Resource):
    def get(self):
        ...
        
    
    def post(self) -> jsonify:
        if UsersModel.add(request=UsersRequest.get()):
            return jsonify({"message": "Usuário adcionado com sucesso!"})
        return jsonify({"error": "Erro ao adcionar novo usuário!"})