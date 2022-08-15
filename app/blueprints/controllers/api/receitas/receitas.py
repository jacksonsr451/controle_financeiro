from flask import jsonify, request
from flask_restful import Resource, reqparse

from ....requets.receitas_request import ReceitasRequest
from ....serializer.receitas_schema import ReceitasSchema

from app.models import ReceitasModel



class Receitas(Resource):
    def get(self) -> jsonify:
        response = None
        if "descricao" in request.args:
            response = self.get_response_on_receitas(
                ReceitasModel.filter_by_descicao(request.args["descricao"]))
        else:        
            response = self.get_response_on_receitas(ReceitasModel.all())
        return response
    
    
    def get_response_on_receitas(self, receitas) -> jsonify:
        if receitas is not None and len(receitas) > 1:
            return jsonify(ReceitasSchema(data=receitas, many=True).data)
        elif receitas is not None and len(receitas) == 1:
            return jsonify(ReceitasSchema(receitas[0]).data)
        return jsonify({"message": "Não há registros em receitas"})
    
    
    def post(self) -> jsonify:
        if ReceitasModel.add(request=ReceitasRequest.get()):
            return jsonify({"message": "Dados inseridos com sucesso"})
        return jsonify({"message": "Não é permitido salvar, verifique os dados inseridos e se não são repeditos!"})
