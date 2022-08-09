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
        if not self.validate_despesas_by_post(despesas=despesas, req_request=req_request):
            return jsonify({"message": "Não é permitido salvar, verifique os dados inseridos e se não são repeditos!"})
        elif DespesasModel.add(request=req_request):
            return jsonify({"message": "Dados inseridos com sucesso"})    
    
        
    def validate_despesas_by_post(self, despesas, req_request) -> bool:
        if len(despesas) > 0:
            for despesa in despesas:
                data_atual = despesa.data.__str__().split('-')
                if despesa.descricao.__eq__(req_request["descricao"]):
                    if data_atual[1].__eq__(req_request["data"].split('-')[1])  \
                        and data_atual[0].__eq__(req_request["data"].split('-')[0]):
                        return False
        return True


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
        if self.validate_despesa_by_put(
            despesas=DespesasModel.all(), req_request=req_request) and  \
                DespesasModel.put(id, req_request):
            return jsonify({"message": "Dados atualizado"})  
        return jsonify({"message": "Não é permitido atualizar, verifique os dados inseridos e se não são repeditos!"})
        
        
    def validate_despesa_by_put(self, despesas, req_request) -> bool:
        if len(despesas) > 0:
            for despesa in despesas:
                data_atual = despesa.data.__str__().split('-')
                if despesa.descricao.__eq__(req_request["descricao"]):
                    if data_atual[1].__eq__(req_request["data"].split('-')[1])  \
                        and data_atual[0].__eq__(req_request["data"].split('-')[0]):
                        return False
        return True


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