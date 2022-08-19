from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.users_model import UsersModel

from ....requets.despesas_request import DespesasRequest
from ....serializer.despesas_schema import DespesasSchema

from app.models.despesas_model import DespesasModel



class Despesas(Resource):
    @jwt_required()
    def get(self) -> jsonify:
        if "descricao" in request.args:
            return self.get_response_on_despesas(
                DespesasModel.filter_by_descicao(request.args["descricao"]))       
        return self.get_response_on_despesas(DespesasModel.all())
    
    
    @jwt_required()
    def get_response_on_despesas(self, despesas) -> jsonify:
        if len(despesas) > 1:
            return jsonify(DespesasSchema(data=despesas, many=True).data)
        elif len(despesas) == 1:
            return jsonify(DespesasSchema(data=despesas[0]).data)
        return jsonify({"message": "Não há registros em despesas"})
    
    
    @jwt_required()
    def post(self) -> jsonify:
        req_request = DespesasRequest.get()
        user = UsersModel.get_user_by_email(email=get_jwt_identity()["email"])
        if DespesasModel.add_user_id(user_id=user.id).add(request=req_request):
            return jsonify({"message": "Dados inseridos com sucesso"})    
        return jsonify({"message": "Não é permitido salvar, verifique os dados inseridos e se não são repeditos!"})
    