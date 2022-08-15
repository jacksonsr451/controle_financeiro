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
        if ReceitasModel.put(id, put_request):    
            return jsonify({"message": "Dados atualizado"})  
        return jsonify({"message": "Não é permitido atualizar, verifique os dados inseridos e se não são repeditos!".format(id)})
        