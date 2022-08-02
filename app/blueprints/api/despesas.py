from flask import jsonify
from flask_restful import Resource, reqparse

from app.models.despesas_model import DespesasModel
from app.ext.flask_sqlalchemy import db
from app.serializer.despesas_schema import DespesasSchema


despesa_post_request = reqparse.RequestParser()
despesa_post_request.add_argument("descricao", type=str, help="Descricao é um campor obrigatório e do tipo str.", required=True)
despesa_post_request.add_argument("valor", type=str, help="Valor é um campor obrigatório e do tipo str.", required=True)
despesa_post_request.add_argument("data", help="Data é um campor obrigatório.", required=True)


despesa_schema = DespesasSchema()
despesas_schema = DespesasSchema(many=True)



class Despesas(Resource):
    def get(self):
        despesas = DespesasModel.query.all()
        if despesas is not None and len(despesas) > 1:
            return jsonify(despesas_schema.dump(despesas))
        elif despesas is not None and len(despesas) == 1:
            return jsonify(despesa_schema.dump(despesas[0]))
        return jsonify({"message": "Não há registros em receitas"})
    
    
    def post(self):
        request = despesa_post_request.parse_args()
        despesas = DespesasModel.query.all()
        if not self.validate_despesas_by_post(despesa=despesas, request=request):
            return jsonify({"message": "Não é permitido salvar, verifique os dados inseridos e se não são repeditos!"})
        new_despesas = DespesasModel(descricao=request["descricao"], valor=request["valor"], data=request["data"])
        db.session.add(new_despesas)
        db.session.commit()
        return jsonify({"message": "Dados inseridos com sucesso"})
        
        
    def validate_despesas_by_post(self, despesas, request) -> bool:
        if len(despesas) > 0:
            for despesa in despesas:
                data_atual = despesa.data.__str__().split('-')
                if despesa.descricao.__eq__(request["descricao"]):
                    if data_atual[1].__eq__(request["data"].split('-')[1]):
                        return False
        return True
