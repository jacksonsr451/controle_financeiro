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
        self.data = self.convert_params_by_datetime(data)
        
    
    @staticmethod
    def convert_params_by_datetime(value) -> datetime:
        if type(value) is str:
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        return ReceitasModel.convert_params_by_datetime(value.strftime("%Y-%m-%d %H:%M:%S"))
    
    
    @staticmethod
    def filter_by_descicao(descricao) -> list:
        return ReceitasModel.query.filter(
                    ReceitasModel.descricao.like(
                        "%{}%".format(descricao))
                    ).all()
        
    
    
    @staticmethod
    def filter_by_ano_and_mes(ano, mes) -> list:
        return ReceitasModel.query.filter(
                    ReceitasModel.data.like(
                        "%{}-{}%".format(ano, mes))
                    ).all()
    
    
    @staticmethod
    def all() -> list:
        return ReceitasModel.query.all()
    
    
    @staticmethod
    def add(request) -> bool:
        try:
            new_receita = ReceitasModel(descricao=request["descricao"], 
                                        valor=request["valor"], 
                                        data=request["data"])
            db.session.add(new_receita)
            db.session.commit()
            return True
        except:
            return False
            
            
    @staticmethod
    def get(id) -> dict:
        receita = ReceitasModel.query.get(id)
        return receita
    
    
    @staticmethod
    def put(id, values) -> bool:
        data = ReceitasModel.get(id)
        if data:    
            data.descricao = values["descricao"]
            data.valor = values["valor"]
            data.data = ReceitasModel.convert_params_by_datetime(values["data"])
            db.session.commit()
            return True
        return False
        
        
    @staticmethod
    def delete(id) -> bool:
        receita = ReceitasModel.get(id)
        if receita is not None:
            db.session.delete(receita)
            db.session.commit()
            return True
        return False
    
    
    def __repr__(self) -> str:
        return "{}".format({
            "id": self.id,
            "descrição": self.descricao,
            "valor": self.valor,
            "data": self.data
        })
    