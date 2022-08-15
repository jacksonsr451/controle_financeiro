from flask import jsonify, request
from flask_restful import Resource, reqparse

from ....requets.despesas_request import DespesasRequest
from ....serializer.despesas_schema import DespesasSchema

from app.models.despesas_model import DespesasModel



class DespesasByID(Resource):
    def get(self, id):
        despesa = DespesasModel.get(id)
        if despesa is not None: return jsonify(DespesasSchema(data=despesa).data)
        return jsonify({"message": "Registro não existe para este id: {}".format(id)})
    
    
    def delete(self, id):
        if DespesasModel.delete(id):
            return jsonify({"success": "Registro deletado com sucesso para o id: {}".format(id)})
        return jsonify({"message": "Registro não existe para este id: {}".format(id)})
    
    
    def put(self, id):    
        req_request = DespesasRequest.get()
        if DespesasModel.get(id) is None:
            return jsonify({"message": "Não há registro para despesas de id: {}".format(id)})  
        if DespesasModel.put(id, req_request):
            return jsonify({"message": "Dados atualizado"})  
        return jsonify({"message": "Não é permitido atualizar, verifique os dados inseridos e se não são repeditos!"})
