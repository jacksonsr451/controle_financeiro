from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from ....serializer.receitas_schema import ReceitasSchema

from app.models import ReceitasModel



class ReceitasByAnoEMes(Resource):
    @jwt_required()
    def get(self, ano, mes):
        return self.get_response_on_receitas(
            ReceitasModel.filter_by_ano_and_mes(ano=ano, mes=mes)
        )
    
    
    @jwt_required()
    def get_response_on_receitas(self, receitas) -> jsonify:
        if receitas is not None and len(receitas) > 1:
            return jsonify(ReceitasSchema(data=receitas, many=True).data)
        elif receitas is not None and len(receitas) == 1:
            return jsonify(ReceitasSchema(data=receitas[0]).data)
        return jsonify({"message": "Não há registros em receitas"})
    