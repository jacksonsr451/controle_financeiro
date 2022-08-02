from flask import jsonify
from flask_restful import Resource, reqparse

from app.models import ReceitasModel
from app.ext.flask_sqlalchemy import db
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
    def get(self):
        receitas = ReceitasModel.query.all()
        if receitas is not None and len(receitas) > 1:
            return jsonify(receitas_schema.dump(receitas))
        elif receitas is not None and len(receitas) == 1:
            return jsonify(receita_schema.dump(receitas[0]))
        return jsonify({"message": "Não há registros em receitas"})
    
    
    def post(self):
        request = receita_post_request.parse_args()
        receitas = ReceitasModel.query.all()
        if not self.validate_receitas_by_post(receitas=receitas, request=request):
            return jsonify({"message": "Não é permitido salvar, verifique os dados inseridos e se não são repeditos!"})
        new_receita = ReceitasModel(descricao=request["descricao"], valor=request["valor"], data=request["data"])
        db.session.add(new_receita)
        db.session.commit()
        return jsonify({"message": "Dados inseridos com sucesso"})
        
        
    def validate_receitas_by_post(self, receitas, request) -> bool:
        if len(receitas) > 0:
            for receita in receitas:
                data_atual = receita.data.__str__().split('-')
                if receita.descricao.__eq__(request["descricao"]):
                    if data_atual[1].__eq__(request["data"].split('-')[1]):
                        return False
        return True



class ReceitaByID(Resource):
    def get(self, id):
        receita = ReceitasModel.query.get(id)
        if receita is not None:
            return jsonify(receita_schema.dump(receita))
        return jsonify({"message": "Registro não existe para este id: {}".format(id)})
        
        
    def delete(self, id):
        receita = ReceitasModel.query.get(id)
        if receita is not None:
            db.session.delete(receita)
            db.session.commit()
            return jsonify({"success": "Registro deletado com sucesso para o id: {}".format(id)})
        return jsonify({"message": "Registro não existe para este id: {}".format(id)})
        
    
    def put(self, id):    
        request = receita_put_request.parse_args()
        receita = ReceitasModel.query.get(id)
        if receita is not None and self.validate_receita_by_put(receita=receita, request=request):
            receita.descricao = request["descricao"]
            receita.valor = request["valor"]
            receita.data = ReceitasModel.convert_params_by_datetime(request["data"])
            db.session.commit()    
            return jsonify({"message": "Dados atualizado"})
        if receita is None:
            return jsonify({"message": "Não há registro para receita de id: {}".format(id)})    
        return jsonify({"message": "Erro ao alualizar receita de id: {}".format(id)})
        
        
    def validate_receita_by_put(self, receita, request) -> bool:
        data_atual = receita.data.__str__().split('-')
        if receita.descricao.__eq__(request["descricao"]):
            if data_atual[1].__eq__(request["data"].split('-')[1]):
                return False
        return True