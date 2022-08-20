from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.users_model import UsersModel

from ....requets.receitas_request import ReceitasRequest
from ....serializer.receitas_schema import ReceitasSchema

from app.models import ReceitasModel


class ReceitaByID(Resource):
    @jwt_required()
    def get(self, id) -> jsonify:
        receita = ReceitasModel.get(id)
        if receita is not None:
            return jsonify(ReceitasSchema(data=receita).data)
        return jsonify(
            {'message': 'Registro não existe para este id: {}'.format(id)}
        )

    @jwt_required()
    def delete(self, id) -> jsonify:
        if ReceitasModel.delete(id):
            return jsonify(
                {
                    'success': 'Registro deletado com sucesso para o id: {}'.format(
                        id
                    )
                }
            )
        return jsonify(
            {'error': 'Registro não existe para este id: {}'.format(id)}
        )

    @jwt_required()
    def put(self, id) -> jsonify:
        user = UsersModel.get_user_by_email(email=get_jwt_identity()['email'])
        put_request = ReceitasRequest.get()
        if ReceitasModel.get(id) is None:
            return jsonify(
                {'error': 'Não há registro para receitas de id: {}'.format(id)}
            )
        if ReceitasModel.add_user_id(user_id=user.id).put(id, put_request):
            return jsonify({'message': 'Dados atualizado'})
        return jsonify(
            {
                'error': 'Não é permitido atualizar, verifique os dados inseridos e se não são repeditos!'.format(
                    id
                )
            }
        )
