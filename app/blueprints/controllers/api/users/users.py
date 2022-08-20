from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.blueprints.middlewares.superuser_middleware import (
    superuser_middleware,
)

from ....serializer.users_schema import UsersSchema

from ....requets.users_request import UsersRequest

from .....models.users_model import UsersModel


class Users(Resource):
    @jwt_required()
    @superuser_middleware
    def get(self) -> jsonify:
        users = UsersModel.all()
        if len(users) != 0:
            return jsonify(UsersSchema(data=users, many=True).data)
        else:
            return jsonify({'error': 'Não há usuários cadastrados!'})

    def post(self) -> jsonify:
        if UsersModel.add(request=UsersRequest.get()):
            return jsonify({'message': 'Usuário adcionado com sucesso!'})
        return jsonify({'error': 'Erro ao adcionar novo usuário!'})
