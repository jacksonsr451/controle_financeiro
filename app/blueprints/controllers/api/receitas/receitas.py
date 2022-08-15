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
            return jsonify(receitas_schema.dump(receitas))
        elif receitas is not None and len(receitas) == 1:
            return jsonify(receita_schema.dump(receitas[0]))
        return jsonify({"message": "Não há registros em receitas"})
    
    
    def post(self) -> jsonify:
        if ReceitasModel.add(request=receita_post_request.parse_args()):
            return jsonify({"message": "Dados inseridos com sucesso"})
        return jsonify({"message": "Não é permitido salvar, verifique os dados inseridos e se não são repeditos!"})
