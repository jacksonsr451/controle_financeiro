from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db
from app.models.users_model import UsersModel



class TestGetByIDDespesa(TestCase):
    URL = "http://localhost:5000/api/v1/usuarios/"
    
    
    def setUp(self) -> None:
        app_test = app.create_app(FORCE_ENV_FOR_DYNACONF="testing")
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()
    
    
    def test_should_be_return_data_by_id(self):
        UsersModel.add(request={"username":"username", "email":"email@email.com", "password": "123456"})
        response = self.app.get(self.URL + "1")
        self.assertEqual(response.get_json(), {
            "id": 1, "username": "username", "email": "email@email.com"
        })
    
    
    def test_should_be_return_message_error(self):
        response = self.app.get(self.URL + "1")
        self.assertEqual(response.get_json(), {
            "error": "Registro não existe para este id: 1"
        })
        
        
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
        