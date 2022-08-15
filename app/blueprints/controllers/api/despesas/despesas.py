from flask import jsonify, request
from flask_restful import Resource, reqparse

from ....requets.despesas_request import DespesasRequest
from ....serializer.despesas_schema import DespesasSchema

from app.models.despesas_model import DespesasModel



class Despesas(Resource):
    def get(self) -> jsonify:
        if "descricao" in request.args:
            return self.get_response_on_despesas(
                DespesasModel.filter_by_descicao(request.args["descricao"]))       
        return self.get_response_on_despesas(DespesasModel.all())
    
    
    def get_response_on_despesas(self, despesas) -> jsonify:
        if despesas is not None and len(despesas) > 1:
            return jsonify(DespesasSchema(data=despesas, many=True).data)
        elif despesas is not None and len(despesas) == 1:
            return jsonify(DespesasSchema(data=despesas).data)
        return jsonify({"message": "Não há registros em despesas"})
    
    
    def post(self) -> jsonify:
        req_request = DespesasRequest.get()
        if DespesasModel.add(request=req_request):
            return jsonify({"message": "Dados inseridos com sucesso"})    
        return jsonify({"message": "Não é permitido salvar, verifique os dados inseridos e se não são repeditos!"})
    

