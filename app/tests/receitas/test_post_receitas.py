from datetime import datetime
from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db
from app.models.receitas_model import ReceitasModel



class TestPostAllReceitas(TestCase):
    URL = "http://localhost:5000/api/v1/receitas"
    
    
    def setUp(self) -> None:
        app_test = app.create_app(FORCE_ENV_FOR_DYNACONF="testing")
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()
        
        
    def test_should_be_create_a_receita_and_return_message_and_status_code(self):
        data_1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        value = jsonify({"message": "Dados inseridos com sucesso"})
        data = {"descricao": "descricao 1", "valor": "100,00", "data": data_1}
        response = self.app.post(self.URL, json=data)
        self.assertEqual(value.get_json(), response.get_json())
        self.assertEqual(response.status_code, 200)
        
        
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
        