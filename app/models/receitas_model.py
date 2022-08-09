from ast import Return
from flask import jsonify
from datetime import datetime
from app.ext.flask_sqlalchemy import db



class ReceitasModel(db.Model):
    __tablename__ = "receitas"
    
    id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.Text, nullable=False)
    valor = db.Column(db.String(50), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    
    
    def __init__(self, descricao, valor, data) -> None:
        self.descricao = descricao
        self.valor = valor
        if type(data) is not datetime:
            self.data = self.convert_params_by_datetime(data)
        else:
            self.data = data
        
    
    @staticmethod
    def convert_params_by_datetime(value):
        if type(value) is str:
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        return value
    
    
    @staticmethod
    def filter_by_descicao(descricao):
        return ReceitasModel.query.filter(
                    ReceitasModel.descricao.like(
                        "%{}%".format(descricao))
                    ).all()
    
    
    @staticmethod
    def all():
        return ReceitasModel.query.all()
    
    
    @staticmethod
    def add(request) -> bool:
        try:
            new_receita = ReceitasModel(descricao=request["descricao"], valor=request["valor"], data=request["data"])
            db.session.add(new_receita)
            db.session.commit()
            return True
        except:
            return False
            
            
    @staticmethod
    def get(id) -> object:
        receita = ReceitasModel.query.get(id)
        return receita
    
    
    @staticmethod
    def put(data, values):
        data.descricao = values["descricao"]
        data.valor = values["valor"]
        data.data = ReceitasModel.convert_params_by_datetime(values["data"])
        db.session.commit()
    
    
    def __repr__(self) -> str:
        return "{}".format({
            "id": self.id,
            "descrição": self.descricao,
            "valor": self.valor,
            "data": self.data
        })
    