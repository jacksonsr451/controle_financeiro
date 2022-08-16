from datetime import datetime
from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db
from app.models.despesas_model import DespesasModel
from ...models.users_model import UsersModel



class TestPutDespesas(TestCase):
    URL = "http://localhost:5000/api/v1/despesas/"
    
    
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
        data_1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        id = "1"
        value = jsonify({"message": "Não há registro para despesas de id: 1"})
        response = self.app.put(self.URL + id, json={
            "categoria": "Outros", "descricao": "descricao 1", "valor": "100,00", "data": data_1
        }, headers={'Authorization': 'Bearer '+self.token})
        self.assertEqual(value.get_json(), response.get_json())
        
        
    def test_should_be_return_message_success(self):
        data_1 = datetime.now()
        DespesasModel.add(request={"descricao":"Primeita despesa", "valor":"200,00", "data":data_1})
        id = "1"
        value = jsonify({"message": "Dados atualizado"})
        response = self.app.put(self.URL + id, json={
            "categoria": "Outros", "descricao": "descricao 1", "valor": "100,00", "data": data_1.strftime("%Y-%m-%d %H:%M:%S")
        }, headers={'Authorization': 'Bearer '+self.token})
        self.assertEqual(value.get_json(), response.get_json())
    
    
    def test_should_be_return_message_duplicate_data(self):
        data_1 = datetime.now()
        DespesasModel.add(request={"descricao":"Primeita despesa", "valor":"200,00", "data":data_1})
        DespesasModel.add(request={"descricao":"Segunda despesa", "valor":"300,00", "data":data_1})
        id = "2"
        value = jsonify({"message": "Não é permitido atualizar, verifique os dados inseridos e se não são repeditos!"}) 
        response = self.app.put(self.URL + id, json={
            "categoria": "Outros", "descricao": "Primeita despesa", "valor": "300,00", "data": data_1.strftime("%Y-%m-%d %H:%M:%S")
        }, headers={'Authorization': 'Bearer '+self.token})
        self.assertEqual(value.get_json(), response.get_json())
    
        
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
        