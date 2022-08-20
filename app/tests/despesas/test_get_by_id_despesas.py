from datetime import datetime
from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db
from app.models.despesas_model import DespesasModel
from ...models.users_model import UsersModel


class TestGetByIDDespesa(TestCase):
    URL = 'http://localhost:5000/api/v1/despesas/'

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

    def test_should_be_return_data_by_id(self):
        data_1 = datetime.now()
        DespesasModel.add(
            request={
                'descricao': 'Primeira despesa',
                'valor': '200,00',
                'data': data_1,
            }
        )
        value = jsonify(
            {
                'id': 1,
                'categoria': 'Outras',
                'descricao': 'Primeira despesa',
                'valor': '200,00',
                'data': data_1.strftime('%Y-%m-%d %H:%M:%S'),
            }
        )
        response = self.app.get(
            self.URL + '1', headers={'Authorization': 'Bearer ' + self.token}
        )
        self.assertEqual(value.get_json(), response.get_json())

    def test_should_be_return_message_error(self):
        id = '1'
        value = jsonify(
            {'message': 'Registro não existe para este id: {}'.format(id)}
        )
        response = self.app.get(
            self.URL + id, headers={'Authorization': 'Bearer ' + self.token}
        )
        self.assertEqual(value.get_json(), response.get_json())

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
