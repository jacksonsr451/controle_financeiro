from flask import jsonify, request
from flask_restful import Resource, reqparse

from app.models.despesas_model import DespesasModel
from app.blueprints.serializer.despesas_schema import DespesasSchema


despesa_post_request = reqparse.RequestParser()
despesa_post_request.add_argument("categoria", type=str, required=False)
despesa_post_request.add_argument("descricao", type=str, help="Descricao é um campor obrigatório e do tipo str.", required=True)
despesa_post_request.add_argument("valor", type=str, help="Valor é um campor obrigatório e do tipo str.", required=True)
despesa_post_request.add_argument("data", help="Data é um campor obrigatório.", required=True)

despesa_put_request = reqparse.RequestParser()
despesa_put_request.add_argument("categoria", type=str, required=False)
despesa_put_request.add_argument("descricao", type=str, help="Descricao é um campor obrigatório e do tipo str.", required=True)
despesa_put_request.add_argument("valor", type=str, help="Valor é um campor obrigatório e do tipo str.", required=True)
despesa_put_request.add_argument("data", help="Data é um campor obrigatório.", required=True)



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