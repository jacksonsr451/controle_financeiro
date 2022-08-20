from datetime import datetime
from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db
from app.models.receitas_model import ReceitasModel

from ...models.users_model import UsersModel


class TestGetByDescricaoReceitas(TestCase):
    URL = 'http://localhost:5000/api/v1/receitas?descricao='

    def setUp(self) -> None:
        app_test = app.create_app(FORCE_ENV_FOR_DYNACONF='testing')
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()
        self.token = self.get_access_token()

    def get_access_token(self):
        UsersModel.add(
            request={
                'username': 'username',
                'email': 'email@gmail.com',
                'password': '123456',
            }
        )

        return self.app.post(
            '/api/v1/auth/login',
            json={'email': 'email@gmail.com', 'password': '123456'},
        ).get_json()['token']

    def test_should_be_filter_by_args_descricao(self):
        data_1 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.app.post(
            '/api/v1/receitas',
            json={
                'descricao': 'Primeira receita',
                'valor': '200,00',
                'data': data_1,
            },
            headers={'Authorization': 'Bearer ' + self.token},
        )
        value = jsonify(
            {
                'id': 1,
                'descricao': 'Primeira receita',
                'valor': '200,00',
                'data': data_1,
            }
        )
        data = self.app.get(
            self.URL + 'Primeira',
            headers={'Authorization': 'Bearer ' + self.token},
        )
        self.assertEqual(value.get_json(), data.get_json())

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
