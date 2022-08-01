from flask import jsonify, request
from flask_restful import Resource

from app.models import ReceitasModel


class Receita(Resource):
    def get(self):
        receitas = ReceitasModel.query.all() 
        return jsonify({
            "receitas": [
                receita.to_dict() for receita in receitas
            ]
        })
    
    
    def post(self):
        data = request.get_json()
        return jsonify({"message": data["message"]})
    
    