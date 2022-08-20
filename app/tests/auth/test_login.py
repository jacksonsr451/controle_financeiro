from datetime import datetime
from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db
from app.models.users_model import UsersModel


class TestResumo(TestCase):
    URL = 'http://localhost:5000/api/v1/auth/login'

    def setUp(self) -> None:
        app_test = app.create_app(FORCE_ENV_FOR_DYNACONF='testing')
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()

    def test_should_be_return_values_by_ano_and_mes(self):
        UsersModel.add(
            request={
                'username': 'username',
                'email': 'email@gmail.com',
                'password': '123456',
            }
        )
        response = self.app.post(
            self.URL, json={'email': 'email@gmail.com', 'password': '123456'}
        )
        self.assertTrue('token' in response.get_json())

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
