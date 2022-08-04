from datetime import datetime
from unittest import TestCase

from flask import jsonify

from app import app
from app.ext.flask_sqlalchemy import db
from app.models.receitas_model import ReceitasModel



class TestDeleteReceitas(TestCase):
    URL = "http://localhost:5000/api/v1/receitas/"
    
    
    def setUp(self) -> None:
        app_test = app.create_app(FORCE_ENV_FOR_DYNACONF="testing")
        app_test.testing = True
        self.ctx = app_test.app_context()
        self.ctx.push()
        self.app = app_test.test_client()
        db.create_all()
        
        
    def test_should_be_delete_data_and_get_message_success(self):
        data_1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = ReceitasModel("Primeita receita", "200,00", data_1)
        db.session.add(data)
        db.session.commit()
        id = "1"
        value = jsonify({"success": "Registro deletado com sucesso para o id: {}".format(id)})
        response = self.app.delete(self.URL + id)
        self.assertEqual(value.get_json(), response.get_json())
    
        
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
        