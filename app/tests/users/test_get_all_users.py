from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db



class TestAddUsers(TestCase):
    URL = "http://localhost:5000/api/v1/usuarios"
    
    
    def setUp(self) -> None:
        app_test = app.create_app(FORCE_ENV_FOR_DYNACONF="testing")
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()

    
    def test_if_get_all_users(self):
        self.app.post(self.URL, json={
            "username": "newuser", "email": "user@email.com", "password": "123456"
        })
        self.app.post(self.URL, json={
            "username": "newuserasd", "email": "userasd@email.com", "password": "123456"
        })
        response = self.app.get(self.URL)
        self.assertEqual(len(response.get_json()), 2)
        
        
    def test_should_be_return_error(self):
        response = self.app.get(self.URL)
        self.assertEqual(response.get_json(), {
            "error": "Não há usuários cadastrados!"
        })

        
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
        