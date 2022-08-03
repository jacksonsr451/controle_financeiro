import os
from unittest import TestCase
from flask import current_app

from app import app
from app.ext.flask_sqlalchemy import db


class TestGetAllDespesas(TestCase):
    URL = "http://localhost:5000/api/v1/despesas"
        
    
    def setUp(self) -> None:
        app_test = app.create_app()
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()
        
        
    def test_shold_be_request_return_status_code_200(self):
        resp = self.app.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        
        
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
        pass

