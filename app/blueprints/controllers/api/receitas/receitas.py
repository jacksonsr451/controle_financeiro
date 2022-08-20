from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from app.models import ReceitasModel
from app.models.users_model import UsersModel

from ....requets.receitas_request import ReceitasRequest
from ....serializer.receitas_schema import ReceitasSchema


class Receitas(Resource):
    @jwt_required()
    def get(self) -> jsonify:
        if 'descricao' in request.args:
            return self.get_response_on_receitas(
                ReceitasModel.filter_by_descicao(request.args['descricao'])
            )
        return self.get_response_on_receitas(ReceitasModel.all())

    @jwt_required()
    def get_response_on_receitas(self, receitas) -> jsonify:
        if len(receitas) > 1:
            return jsonify(ReceitasSchema(data=receitas, many=True).data)
        elif len(receitas) == 1:
            return jsonify(ReceitasSchema(receitas[0]).data)
        return jsonify({'error': 'Não há registros em receitas'})

    @jwt_required()
    def post(self) -> jsonify:
        user = UsersModel.get_user_by_email(email=get_jwt_identity()['email'])
        if ReceitasModel.add_user_id(user_id=user.id).add(
            request=ReceitasRequest.get()
        ):
            return jsonify({'message': 'Dados inseridos com sucesso'})
        return jsonify(
            {
                'error': 'Não é permitido salvar, verifique os dados inseridos e se não são repeditos!'
            }
        )
