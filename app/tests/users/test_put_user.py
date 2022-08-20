from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db
from app.models.users_model import UsersModel


class TestPutUsers(TestCase):
    URL = 'http://localhost:5000/api/v1/usuarios/'

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
                'username': 'username_teste',
                'email': 'email_teste@gmail.com',
                'password': '123456',
            }
        )

        return self.app.post(
            '/api/v1/auth/login',
            json={'email': 'email_teste@gmail.com', 'password': '123456'},
        ).get_json()['token']

    def test_should_be_return_message_error_data_not_exist_in_db(self):
        response = self.app.put(
            self.URL + '2',
            json={'username': 'username', 'email': 'email@email.com'},
            headers={'Authorization': 'Bearer ' + self.token},
        )
        self.assertEqual(
            response.get_json(),
            {'error': 'Não há registro para usuários de id: 2!'},
        )

    def test_should_be_return_message_success(self):
        UsersModel.add(
            request={
                'username': 'username',
                'email': 'email@email.com',
                'password': '123456',
            }
        )
        response = self.app.put(
            self.URL + '2',
            json={'username': 'username', 'email': 'email@gmail.com'},
            headers={'Authorization': 'Bearer ' + self.token},
        )
        self.assertEqual(
            response.get_json(), {'message': 'Usuário atualizado!'}
        )

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
