from flask import jsonify, request
from flask_restful import Resource, reqparse

from app.models import ReceitasModel
from app.serializer.receitas_schema import ReceitasSchema


receita_post_request = reqparse.RequestParser()
receita_post_request.add_argument("descricao", type=str, help="Descricao é um campor obrigatório e do tipo str.", required=True)
receita_post_request.add_argument("valor", type=str, help="Valor é um campor obrigatório e do tipo str.", required=True)
receita_post_request.add_argument("data", help="Data é um campor obrigatório.", required=True)

receita_put_request = reqparse.RequestParser()
receita_put_request.add_argument("descricao", type=str, help="Descricao é um campor obrigatório e do tipo str.", required=True)
receita_put_request.add_argument("valor", type=str, help="Valor é um campor obrigatório e do tipo str.", required=True)
receita_put_request.add_argument("data", help="Data é um campor obrigatório.", required=True)

receita_schema = ReceitasSchema()
receitas_schema = ReceitasSchema(many=True)



class Receita(Resource):
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
            return jsonify(receitas_schema.dump(receitas))
        elif receitas is not None and len(receitas) == 1:
            return jsonify(receita_schema.dump(receitas[0]))
        return jsonify({"message": "Não há registros em receitas"})
    
    
    def post(self) -> jsonify:
        receitas = ReceitasModel.all()
        if not self.validate_receitas_by_post(
            receitas=receitas, req_request=receita_post_request.parse_args()):
            return jsonify({"message": "Não é permitido salvar, verifique os dados inseridos e se não são repeditos!"})
        if ReceitasModel.add(request=receita_post_request.parse_args()):
            return jsonify({"message": "Dados inseridos com sucesso"})
        
        
    def validate_receitas_by_post(self, receitas, req_request) -> bool:
        if len(receitas) > 0:
            for receita in receitas:
                data_atual = receita.data.__str__().split('-')
                if receita.descricao.__eq__(req_request["descricao"]):
                    if data_atual[1].__eq__(req_request["data"].split('-')[1])  \
                        and data_atual[0].__eq__(req_request["data"].split('-')[0]):
                        return False
        return True



class ReceitaByID(Resource):
    def get(self, id) -> jsonify:
        receita = ReceitasModel.get(id)
        if receita is not None: return jsonify(receita_schema.dump(receita))
        return jsonify({"message": "Registro não existe para este id: {}".format(id)})
        
        
    def delete(self, id) -> jsonify:
        if ReceitasModel.delete(id):
            return jsonify({"success": "Registro deletado com sucesso para o id: {}".format(id)})
        return jsonify({"message": "Registro não existe para este id: {}".format(id)})
        
    
    def put(self, id) -> jsonify:    
        put_request = receita_put_request.parse_args()
        if ReceitasModel.get(id) is None:
            return jsonify({"message": "Não há registro para receitas de id: {}".format(id)})  
        if self.validate_receita_by_put(
            receitas=ReceitasModel.all(), 
            req_request=put_request) and ReceitasModel.put(id, put_request):    
            return jsonify({"message": "Dados atualizado"})  
        return jsonify({"message": "Não é permitido atualizar, verifique os dados inseridos e se não são repeditos!".format(id)})
        
        
    def validate_receita_by_put(self, receitas, req_request) -> bool:
        if len(receitas) > 0:
            for receita in receitas:
                data_atual = receita.data.__str__().split('-')
                if receita.descricao.__eq__(req_request["descricao"]):
                    if data_atual[1].__eq__(req_request["data"].split('-')[1]) and data_atual[0].__eq__(req_request["data"].split('-')[0]):
                        return False
        return True


class ReceitasByAnoEMes(Resource):
    def get(self, ano, mes):
        return self.get_response_on_receitas(
            ReceitasModel.filter_by_ano_and_mes(ano=ano, mes=mes)
        )
    
    
    def get_response_on_receitas(self, receitas) -> jsonify:
        if receitas is not None and len(receitas) > 1:
            return jsonify(receitas_schema.dump(receitas))
        elif receitas is not None and len(receitas) == 1:
            return jsonify(receita_schema.dump(receitas[0]))
        return jsonify({"message": "Não há registros em receitas"})
    