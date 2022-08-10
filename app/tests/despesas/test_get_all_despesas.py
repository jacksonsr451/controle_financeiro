from datetime import datetime
from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db
from app.models.despesas_model import DespesasModel



class TestGetAllDespesas(TestCase):
    URL = "http://localhost:5000/api/v1/despesas"
        
    
    def setUp(self) -> None:
        app_test = app.create_app(FORCE_ENV_FOR_DYNACONF="testing")
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()
        
    
    def test_should_be_return_message_error(self):
        value = jsonify({"message": "Não há registros em despesas"})
        response = self.app.get(self.URL)
        self.assertEqual(value.get_json(), response.get_json())
        
        
    def test_should_be_request_return_status_code_200(self):
        response = self.app.get(self.URL)
        self.assertEqual(response.status_code, 200)
        
    
    @staticmethod
    def include_data(data_1, data_2):
        DespesasModel.add(request={"descricao":"Primeiro dado", "valor":"200,00", "data":data_1})
        DespesasModel.add(request={"descricao":"Segundo dado", "valor":"200,00", "data":data_2})
        
    
    @staticmethod
    def get_json_test_response_is_equal(data_1, data_2):
        return jsonify([
            {
                "id": 1,
                "categoria": "Outras",
                "descricao": "Primeiro dado",
                "valor": "200,00",
                "data": data_1.strftime("%Y-%m-%d %H:%M:%S")
            },
            {
                "id": 2,
                "categoria": "Outras",
                "descricao": "Segundo dado",
                "valor": "200,00",
                "data": data_2.strftime("%Y-%m-%d %H:%M:%S")
            }
        ])
    
        
    def test_should_be_response_is_equal(self):
        data_1 = datetime.now()
        data_2 = datetime.now()
        self.include_data(data_1, data_2)
        value = self.get_json_test_response_is_equal(data_1, data_2)
        response = self.app.get(self.URL)
        self.assertEqual(value.get_json(), response.get_json())
        
        
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

