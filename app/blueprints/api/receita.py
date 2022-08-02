from datetime import datetime
import json
from flask import jsonify
from flask_restful import Resource, reqparse, inputs

from app.models import ReceitasModel
from app.ext.flask_sqlalchemy import db


receita_post_request = reqparse.RequestParser()
receita_post_request.add_argument("id", type=int, help="Id é um campor obrigatório e do tipo int.", required=True)
receita_post_request.add_argument("descricao", type=str, help="Descricao é um campor obrigatório e do tipo str.", required=True)
receita_post_request.add_argument("valor", type=str, help="Valor é um campor obrigatório e do tipo str.", required=True)
receita_post_request.add_argument("data", help="Data é um campor obrigatório.", required=True)


class Receita(Resource):
    def get(self):
        receitas = ReceitasModel.query.all() 
        list_receitas: list = list()
        for receita in receitas:
            list_receitas.append(receita.as_dict())
        return jsonify(list_receitas)
    
    
    def post(self):
        request = receita_post_request.parse_args()
        receitas = ReceitasModel.query.all() 
        if len(receitas) > 0:
            for receita in receitas:
                if receitas["descricao"] == request["descricao"]:
                    if receita["data"] == request["data"]:
                        return jsonify({"message": "Não é permitido salvar aqui"})
        new_receita = ReceitasModel(id=request["id"], descricao=request["descricao"], valor=request["valor"], data=request["data"])
        db.session.add(new_receita)
        db.session.commit()