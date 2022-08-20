from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db


class TestAddUsers(TestCase):
    URL = 'http://localhost:5000/api/v1/usuarios'

    def setUp(self) -> None:
        app_test = app.create_app(FORCE_ENV_FOR_DYNACONF='testing')
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()

    def test_should_be_add_user(self):
        response = self.app.post(
            self.URL,
            json={
                'username': 'newuser',
                'email': 'user@email.com',
                'password': '123456',
            },
        )
        self.assertEqual(
            response.get_json(), {'message': 'Usuário adcionado com sucesso!'}
        )

    def test_should_be_return_error(self):
        self.app.post(
            self.URL,
            json={
                'username': 'newuser',
                'email': 'user@email.com',
                'password': '123456',
            },
        )
        response = self.app.post(
            self.URL,
            json={
                'username': 'newuser',
                'email': 'user@email.com',
                'password': '123456',
            },
        )
        self.assertEqual(
            response.get_json(), {'error': 'Erro ao adcionar novo usuário!'}
        )

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
