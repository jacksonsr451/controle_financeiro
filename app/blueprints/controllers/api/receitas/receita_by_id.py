from flask import jsonify, request
from flask_restful import Resource, reqparse

from ....requets.receitas_request import ReceitasRequest
from ....serializer.receitas_schema import ReceitasSchema

from app.models import ReceitasModel



class ReceitaByID(Resource):
    def get(self, id) -> jsonify:
        receita = ReceitasModel.get(id)
        if receita is not None: return jsonify(ReceitasSchema(data=receita).data)
        return jsonify({"message": "Registro não existe para este id: {}".format(id)})
        
        
    def delete(self, id) -> jsonify:
        if ReceitasModel.delete(id):
            return jsonify({"success": "Registro deletado com sucesso para o id: {}".format(id)})
        return jsonify({"message": "Registro não existe para este id: {}".format(id)})
        
    
    def put(self, id) -> jsonify:    
        put_request = ReceitasRequest.get()
        if ReceitasModel.get(id) is None:
            return jsonify({"message": "Não há registro para receitas de id: {}".format(id)})  
        if ReceitasModel.put(id, put_request):    
            return jsonify({"message": "Dados atualizado"})  
        return jsonify({"message": "Não é permitido atualizar, verifique os dados inseridos e se não são repeditos!".format(id)})
        