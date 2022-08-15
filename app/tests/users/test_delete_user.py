from unittest import TestCase
from urllib import response

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db



class TestAddUsers(TestCase):
    URL = "http://localhost:5000/api/v1/usuarios/"
    
    
    def setUp(self) -> None:
        app_test = app.create_app(FORCE_ENV_FOR_DYNACONF="testing")
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()

    
    def test_should_be_delete_user(self):
        self.app.post("/api/v1/usuarios", json={
            "username": "newuser", "email": "user@email.com", "password": "123456"
        })
        response = self.app.delete(self.URL + "1")
        self.assertEqual(response.get_json(), {
            "message": "Usuário deletado com sucesso!"
        })
        
        
    def test_should_be_return_error(self):
        response = self.app.delete(self.URL + "1")
        self.assertEqual(response.get_json(), {
            "error": "Não usuário cadastrado com o id: 1!"
        })
    
        
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
        