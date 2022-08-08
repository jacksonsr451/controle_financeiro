from datetime import datetime
from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db
from app.models.receitas_model import ReceitasModel



class TestGetByDescricaoReceitas(TestCase):
    URL = "http://localhost:5000/api/v1/receitas?descricao="
    
    
    def setUp(self) -> None:
        app_test = app.create_app(FORCE_ENV_FOR_DYNACONF="testing")
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()
        
    
    def test_should_be_filter_by_args_descricao(self):
        self.app.get(self.URL + "1")
        
        
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
