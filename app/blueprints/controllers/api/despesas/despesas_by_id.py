from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from app.models.despesas_model import DespesasModel
from app.models.users_model import UsersModel

from ....requets.despesas_request import DespesasRequest
from ....serializer.despesas_schema import DespesasSchema


class DespesasByID(Resource):
    @jwt_required()
    def get(self, id):
        despesa = DespesasModel.get(id)
        if despesa is not None:
            return jsonify(DespesasSchema(data=despesa).data)
        return jsonify(
            {'message': 'Registro não existe para este id: {}'.format(id)}
        )

    @jwt_required()
    def delete(self, id):
        if DespesasModel.delete(id):
            return jsonify(
                {
                    'success': 'Registro deletado com sucesso para o id: {}'.format(
                        id
                    )
                }
            )
        return jsonify(
            {'message': 'Registro não existe para este id: {}'.format(id)}
        )

    @jwt_required()
    def put(self, id):
        req_request = DespesasRequest.get()
        user = UsersModel.get_user_by_email(email=get_jwt_identity()['email'])
        if DespesasModel.get(id) is None:
            return jsonify(
                {
                    'message': 'Não há registro para despesas de id: {}'.format(
                        id
                    )
                }
            )
        if DespesasModel.add_user_id(user_id=user.id).put(id, req_request):
            return jsonify({'message': 'Dados atualizado'})
        return jsonify(
            {
                'message': 'Não é permitido atualizar, verifique os dados inseridos e se não são repeditos!'
            }
        )
