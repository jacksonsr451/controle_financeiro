from datetime import datetime
from unittest import TestCase
from flask import jsonify


from app import app
from app.ext.flask_sqlalchemy import db
from app.models.despesas_model import DespesasModel



class TestGetDespesasByAnoAndMes(TestCase):
    URL = "http://localhost:5000/api/v1/despesas/"
    
    
    def setUp(self) -> None:
        app_test = app.create_app(FORCE_ENV_FOR_DYNACONF="testing")
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()
        
    
    def test_should_be_filter_by_args_ano_and_mes(self):
        data_1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        DespesasModel.add(request={"descricao": "Primeira despesa", "valor":"200,00", "data":data_1})
        value = jsonify({"id": 1, "categoria": "Outras", "descricao":"Primeira despesa", "valor":"200,00", "data":data_1.__str__().replace(" ", "T")})
        data = self.app.get(self.URL + "2022/08")
        self.assertEqual(value.get_json(), data.get_json())
        
        
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
