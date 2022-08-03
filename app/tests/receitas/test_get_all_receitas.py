from datetime import datetime
from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db
from app.models.receitas_model import ReceitasModel



class TestGetAllReceitas(TestCase):
    URL = "http://localhost:5000/api/v1/receitas"
    
    
    def setUp(self) -> None:
        app_test = app.create_app()
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()
        
    
    def test_should_be_return_message_error(self):
        value = jsonify({"message": "Não há registros em receitas"})
        response = self.app.get(self.URL)
        self.assertEqual(value.get_json(), response.get_json())
            
        
    def test_should_be_request_return_status_code_200(self):
        response = self.app.get(self.URL)
        self.assertEqual(response.status_code, 200)
        
        
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
    