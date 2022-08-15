from flask import jsonify
from flask_restful import Resource

from ....serializer.users_schema import UsersSchema

from ....requets.users_request import UsersRequest

from .....models.users_model import UsersModel




class UsersById(Resource):
    def get(self, id) -> jsonify:
        ...
        
    
    def put(self, id) -> jsonify:
        if UsersModel.put(id, UsersRequest.get()):
            return jsonify({"message": "Usuário atualizado!"})  
        return jsonify({"message": "Não há registro para usuários de id: {}!".format(id)})

        
    def delete(self, id) -> jsonify:
        if UsersModel.delete(id=id):
            return jsonify({"message": "Usuário deletado com sucesso!"})
        return jsonify({"error": "Não usuário cadastrado com o id: {}!".format(id)})
            