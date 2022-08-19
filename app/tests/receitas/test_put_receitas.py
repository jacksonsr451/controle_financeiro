from datetime import datetime
from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db
from app.models.receitas_model import ReceitasModel
from ...models.users_model import UsersModel



class TestPutDespesas(TestCase):
    URL = "http://localhost:5000/api/v1/receitas/"
    
    
    def setUp(self) -> None:
        app_test = app.create_app(FORCE_ENV_FOR_DYNACONF="testing")
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()
        self.token = self.get_access_token()
        
        
    def get_access_token(self):
        UsersModel.add(request={
            "username": "username", "email": "email@gmail.com", "password": "123456"
        })
        
        return self.app.post('/api/v1/auth/login', json={
            'email': "email@gmail.com", "password": "123456"
        }).get_json()["token"]
    
    
    def test_should_be_return_message_error_data_not_exist_in_db(self):
        data_1 = datetime.now()
        data = {"descricao": "descricao 1", "valor": "100,00", "data": data_1}
        id = "1"
        value = jsonify({"error": "Não há registro para receitas de id: 1"})
        response = self.app.put(self.URL + id, json=data, headers={'Authorization': 'Bearer '+self.token})
        self.assertEqual(value.get_json(), response.get_json())
        
        
    def test_should_be_return_message_success(self):
        data_1 = datetime.now()
        ReceitasModel.add(request={"descricao":"Primeita receita", "valor":"200,00", "data":data_1})
        id = "1"
        value = jsonify({"message": "Dados atualizado"})
        response = self.app.put(self.URL + id, json={
            "descricao": "descricao 1", "valor": "100,00", "data": data_1.strftime("%Y-%m-%d %H:%M:%S")
        }, headers={'Authorization': 'Bearer '+self.token})
        self.assertEqual(value.get_json(), response.get_json())
        
        
    def test_should_be_return_message_duplicate_data(self):
        data_1 = datetime.now()
        ReceitasModel.add(request={"descricao":"Primeita receita", "valor":"200,00", "data":data_1})
        ReceitasModel.add(request={"descricao":"Segunda receita", "valor":"300,00", "data":data_1})
        id = "2"
        value = jsonify({"error": "Não é permitido atualizar, verifique os dados inseridos e se não são repeditos!"}) 
        response = self.app.put(self.URL + id, json={
            "descricao": "Primeita receita", "valor": "300,00", "data": data_1.strftime("%Y-%m-%d %H:%M:%S")
        }, headers={'Authorization': 'Bearer '+self.token})
        self.assertEqual(value.get_json(), response.get_json())
    
        
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
        