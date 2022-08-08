from datetime import datetime
from app.ext.flask_sqlalchemy import db
import enum



class CategoriaEnum(enum.Enum):
    ALIMENTACAO = "Alimentação"
    SAUDE = "Saúde"
    MORADIA = "Moradia"
    TRANSPORTE = "Transporte"
    EDUCACAO = "Educação"
    LAZER = "Lazer"
    IMPREVISTOS = "Imprevistos"
    OUTRAS = "Outras"
    


class DespesasModel(db.Model):
    __tablename__ = "despesas"
    
    id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    categoria = db.Column(db.Enum(CategoriaEnum), nullable=False, default=CategoriaEnum.OUTRAS)
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
        
    
    def __repr__(self) -> str:
        return "{}".format({
            "id": self.id,
            "descrição": self.descricao,
            "valor": self.valor,
            "data": self.data
        })
    