from flask import jsonify, request
from flask_restful import Resource, reqparse

from app.models.despesas_model import DespesasModel
from app.serializer.despesas_schema import DespesasSchema


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


despesa_schema = DespesasSchema()
despesas_schema = DespesasSchema(many=True)



class Despesas(Resource):
    def get(self) -> jsonify:
        if "descricao" in request.args:
            return self.get_response_on_despesas(
                DespesasModel.filter_by_descicao(request.args["descricao"]))       
        return self.get_response_on_despesas(DespesasModel.all())
    
    
    def get_response_on_despesas(self, despesas) -> jsonify:
        if despesas is not None and len(despesas) > 1:
            return jsonify(despesas_schema.dump(despesas))
        elif despesas is not None and len(despesas) == 1:
            return jsonify(despesa_schema.dump(despesas[0]))
        return jsonify({"message": "Não há registros em despesas"})
    
    
    def post(self) -> jsonify:
        req_request = despesa_post_request.parse_args()
        despesas = DespesasModel.all()
        if DespesasModel.add(request=req_request):
            return jsonify({"message": "Dados inseridos com sucesso"})    
        return jsonify({"message": "Não é permitido salvar, verifique os dados inseridos e se não são repeditos!"})
    


class DespesasByID(Resource):
    def get(self, id):
        despesa = DespesasModel.get(id)
        if despesa is not None: return jsonify(despesa_schema.dump(despesa))
        return jsonify({"message": "Registro não existe para este id: {}".format(id)})
    
    
    def delete(self, id):
        if DespesasModel.delete(id):
            return jsonify({"success": "Registro deletado com sucesso para o id: {}".format(id)})
        return jsonify({"message": "Registro não existe para este id: {}".format(id)})
    
    
    def put(self, id):    
        req_request = despesa_put_request.parse_args()
        if DespesasModel.get(id) is None:
            return jsonify({"message": "Não há registro para despesas de id: {}".format(id)})  
        if DespesasModel.put(id, req_request):
            return jsonify({"message": "Dados atualizado"})  
        return jsonify({"message": "Não é permitido atualizar, verifique os dados inseridos e se não são repeditos!"})


class DespesasByAnoEMes(Resource):
    def get(self, ano, mes):
        return self.get_response_on_despesas(
            DespesasModel.filter_by_ano_and_mes(ano=ano, mes=mes)
        )
    
    
    def get_response_on_despesas(self, despesas) -> jsonify:
        if despesas is not None and len(despesas) > 1:
            return jsonify(despesas_schema.dump(despesas))
        elif despesas is not None and len(despesas) == 1:
            return jsonify(despesa_schema.dump(despesas[0]))
        return jsonify({"message": "Não há registros em despesas"})