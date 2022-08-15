from flask import jsonify, request
from flask_restful import Resource, reqparse

from app.models.despesas_model import DespesasModel
from app.blueprints.serializer.despesas_schema import DespesasSchema



class DespesasByAnoEMes(Resource):
    def get(self, ano, mes):
        return self.get_response_on_despesas(
            DespesasModel.filter_by_ano_and_mes(ano=ano, mes=mes)
        )
    
    
    def get_response_on_despesas(self, despesas) -> jsonify:
        if despesas is not None and len(despesas) > 1:
            return jsonify(DespesasSchema(despesas, many=True).data)
        elif despesas is not None and len(despesas) == 1:
            return jsonify(DespesasSchema(despesas[0]).data)
        return jsonify({"message": "Não há registros em despesas"})