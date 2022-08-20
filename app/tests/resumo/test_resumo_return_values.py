from datetime import datetime
from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db
from app.models.despesas_model import DespesasModel
from app.models.receitas_model import ReceitasModel

from ...models.users_model import UsersModel


class TestResumo(TestCase):
    URL = 'http://localhost:5000/api/v1/resumo/'

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

    def test_should_be_return_values_by_ano_and_mes(self):
        self.insert_data()
        value = self.get_value()
        response = self.app.get(
            self.URL + '2022/08',
            headers={'Authorization': 'Bearer ' + self.token},
        )
        self.assertEqual(value.get_json(), response.get_json())

    @staticmethod
    def get_value() -> jsonify:
        return jsonify(
            {
                'total receitas': '1200,00',
                'total despesas': '1200,00',
                'saldo final': '0,00',
                'total gasto por categoria': {
                    'Alimentação': '400,00',
                    'Saúde': '400,00',
                    'Moradia': '0,00',
                    'Transporte': '0,00',
                    'Educação': '400,00',
                    'Lazer': '0,00',
                    'Imprevistos': '0,00',
                    'Outras': '0,00',
                },
            }
        )

    @staticmethod
    def insert_data() -> None:
        ReceitasModel.add(
            request={
                'descricao': 'Primeira receita',
                'valor': '200,00',
                'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
        )
        DespesasModel.add(
            request={
                'categoria': 'Alimentação',
                'descricao': 'Primeira despesa',
                'valor': '200,00',
                'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
        )
        ReceitasModel.add(
            request={
                'descricao': 'Segunda receita',
                'valor': '200,00',
                'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
        )
        DespesasModel.add(
            request={
                'categoria': 'Saúde',
                'descricao': 'Segunta despesa',
                'valor': '200,00',
                'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
        )
        ReceitasModel.add(
            request={
                'descricao': 'Terceira receita',
                'valor': '200,00',
                'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
        )
        DespesasModel.add(
            request={
                'categoria': 'Educação',
                'descricao': 'Terceira despesa',
                'valor': '200,00',
                'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
        )
        ReceitasModel.add(
            request={
                'descricao': 'Quarta receita',
                'valor': '200,00',
                'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
        )
        DespesasModel.add(
            request={
                'categoria': 'Alimentação',
                'descricao': 'Quarta despesa',
                'valor': '200,00',
                'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
        )
        ReceitasModel.add(
            request={
                'descricao': 'Quinta receita',
                'valor': '200,00',
                'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
        )
        DespesasModel.add(
            request={
                'categoria': 'Saúde',
                'descricao': 'Quinta despesa',
                'valor': '200,00',
                'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
        )
        ReceitasModel.add(
            request={
                'descricao': 'Sexta receita',
                'valor': '200,00',
                'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
        )
        DespesasModel.add(
            request={
                'categoria': 'Educação',
                'descricao': 'Sexta despesa',
                'valor': '200,00',
                'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
        )

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
