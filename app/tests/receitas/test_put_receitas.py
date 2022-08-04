from datetime import datetime
from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db
from app.models.receitas_model import ReceitasModel



class TestPutDespesas(TestCase):
    URL = "http://localhost:5000/api/v1/receitas/"
    
    
    def setUp(self) -> None:
        app_test = app.create_app(FORCE_ENV_FOR_DYNACONF="testing")
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()
    
    
    def test_should_be_return_message_error_data_not_exist_in_db(self):
        data_1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {"descricao": "descricao 1", "valor": "100,00", "data": data_1}
        id = "1"
        value = jsonify({"message": "Não há registro para receitas de id: 1"})
        response = self.app.put(self.URL + id, json=data)
        self.assertEqual(value.get_json(), response.get_json())
        
        
    def test_should_be_return_message_success(self):
        data_1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = ReceitasModel("Primeita receita", "200,00", data_1)
        db.session.add(data)
        db.session.commit()
        id = "1"
        data_put = {"descricao": "descricao 1", "valor": "100,00", "data": data_1}
        value = jsonify({"message": "Dados atualizado"})
        response = self.app.put(self.URL + id, json=data_put)
        self.assertEqual(value.get_json(), response.get_json())
    
        
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
        