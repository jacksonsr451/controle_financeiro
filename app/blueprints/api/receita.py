from flask import jsonify
from flask_restful import Resource, reqparse

from app.models import ReceitasModel
from app.ext.flask_sqlalchemy import db
from app.serializer.receitas_schema import ReceitasSchema


receita_post_request = reqparse.RequestParser()
receita_post_request.add_argument("descricao", type=str, help="Descricao é um campor obrigatório e do tipo str.", required=True)
receita_post_request.add_argument("valor", type=str, help="Valor é um campor obrigatório e do tipo str.", required=True)
receita_post_request.add_argument("data", help="Data é um campor obrigatório.", required=True)


receita_schema = ReceitasSchema()
receitas_schema = ReceitasSchema(many=True)



class Receita(Resource):
    def get(self):
        return jsonify(receitas_schema.dump(ReceitasModel.query.all()))
    
    
    def post(self):
        request = receita_post_request.parse_args()
        receitas = ReceitasModel.query.all()
        if not self.validate_receitas_by_post(receitas=receitas, request=request):
            return jsonify({"message": "Não é permitido salvar aqui"})
        new_receita = ReceitasModel(descricao=request["descricao"], valor=request["valor"], data=request["data"])
        db.session.add(new_receita)
        db.session.commit()
        
        
    def validate_receitas_by_post(self, receitas, request) -> bool:
        if len(receitas) > 0:
            for receita in receitas:
                data_atual = receita.data.__str__().split('-')
                if receita.descricao.__eq__(request["descricao"]):
                    if data_atual[1].__eq__(request["data"].split('-')[1]):
                        return False
        return True
    