from flask import jsonify
from flask_restful import Resource, reqparse

from app.models.despesas_model import DespesasModel
from app.ext.flask_sqlalchemy import db
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
    def get(self):
        despesas = DespesasModel.query.all()
        if despesas is not None and len(despesas) > 1:
            return jsonify(despesas_schema.dump(despesas))
        elif despesas is not None and len(despesas) == 1:
            return jsonify(despesa_schema.dump(despesas[0]))
        return jsonify({"message": "Não há registros em despesas"})
    
    
    def post(self):
        request = despesa_post_request.parse_args()
        despesas = DespesasModel.query.all()
        if not self.validate_despesas_by_post(despesas=despesas, request=request):
            return jsonify({"message": "Não é permitido salvar, verifique os dados inseridos e se não são repeditos!"})
        if "categoria" in request:
            new_despesas = DespesasModel(categoria=request["categoria"],descricao=request["descricao"], valor=request["valor"], data=request["data"])
        else:
            new_despesas = DespesasModel(descricao=request["descricao"], valor=request["valor"], data=request["data"])
        db.session.add(new_despesas)
        db.session.commit()
        return jsonify({"message": "Dados inseridos com sucesso"})
        
        
    def validate_despesas_by_post(self, despesas, request) -> bool:
        if len(despesas) > 0:
            for despesa in despesas:
                data_atual = despesa.data.__str__().split('-')
                if despesa.descricao.__eq__(request["descricao"]):
                    if data_atual[1].__eq__(request["data"].split('-')[1]) and data_atual[0].__eq__(request["data"].split('-')[0]):
                        return False
        return True


class DespesasByID(Resource):
    def get(self, id):
        despesa = DespesasModel.query.get(id)
        if despesa is not None:
            return jsonify(despesa_schema.dump(despesa))
        return jsonify({"message": "Registro não existe para este id: {}".format(id)})
    
    
    def delete(self, id):
        despesa = DespesasModel.query.get(id)
        if despesa is not None:
            db.session.delete(despesa)
            db.session.commit()
            return jsonify({"success": "Registro deletado com sucesso para o id: {}".format(id)})
        return jsonify({"message": "Registro não existe para este id: {}".format(id)})
    
    
    def put(self, id):    
        request = despesa_put_request.parse_args()
        despesa = DespesasModel.query.get(id)
        if despesa is not None and self.validate_despesa_by_put(despesas=DespesasModel.query.all(), request=request):
            despesa.descricao = request["descricao"]
            despesa.categoria = request["categoria"]
            despesa.valor = request["valor"]
            despesa.data = DespesasModel.convert_params_by_datetime(request["data"])
            db.session.commit()    
            return jsonify({"message": "Dados atualizado"})
        if despesa is None:
            return jsonify({"message": "Não há registro para despesas de id: {}".format(id)})    
        return jsonify({"message": "Não é permitido atualizar, verifique os dados inseridos e se não são repeditos!"})
        
        
    def validate_despesa_by_put(self, despesas, request) -> bool:
        if len(despesas) > 0:
            for despesa in despesas:
                data_atual = despesa.data.__str__().split('-')
                if despesa.descricao.__eq__(request["descricao"]):
                    if data_atual[1].__eq__(request["data"].split('-')[1]) and data_atual[0].__eq__(request["data"].split('-')[0]):
                        return False
        return True
