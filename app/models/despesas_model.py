from datetime import datetime
from app.enum.categoria_enum import CategoriaEnum
from app.ext.flask_sqlalchemy import db
    


class DespesasModel(db.Model):
    __tablename__ = "despesas"
    __table_args__ = (
        db.UniqueConstraint('descricao', 'data', name='unique_descricao_for_data'),
    )
    
    id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    categoria = db.Column(db.Enum(CategoriaEnum), nullable=False, default=CategoriaEnum.OUTRAS)
    descricao = db.Column(db.Text, nullable=False)
    valor = db.Column(db.String(50), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    
    
    def __init__(self, categoria=None, descricao=None, valor=None, data=None) -> None:
        if categoria is not None:
            self.categoria = CategoriaEnum(categoria)
        self.descricao = descricao
        self.valor = valor
        self.data = self.convert_params_by_datetime(data)
            
    
    @staticmethod
    def convert_params_by_datetime(value):
        if type(value) is str:
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        return DespesasModel.convert_params_by_datetime(value.strftime("%Y-%m-%d %H:%M:%S"))
    
    
    @staticmethod
    def all() -> list:
        return DespesasModel.query.all()
    
    
    @staticmethod
    def filter_by_descicao(descricao) -> list:
        return DespesasModel.query.filter(
                    DespesasModel.descricao.like(
                        "%{}%".format(descricao))
                    ).all()

    
    @staticmethod
    def filter_by_ano_and_mes(ano, mes) -> list:
        return DespesasModel.query.filter(
                    DespesasModel.data.like(
                        "%{}-{}%".format(ano, mes))
                    ).all()
        
        
    @staticmethod
    def add(request) -> bool:
        try:
            if "categoria" in request:
                new_despesa = DespesasModel(categoria=request["categoria"], 
                                            descricao=request["descricao"], 
                                            valor=request["valor"], 
                                            data=request["data"])
            else:
                new_despesa = DespesasModel(descricao=request["descricao"], 
                                            valor=request["valor"], 
                                            data=request["data"])
            db.session.add(new_despesa)
            db.session.commit()
            return True
        except:
            return False
        
    
    @staticmethod
    def get(id) -> dict:
        receita = DespesasModel.query.get(id)
        return receita
    
    
    @staticmethod
    def put(id, values) -> bool:
        try:
            data = DespesasModel.get(id)
            data.categoria = values["categoria"]   
            data.descricao = values["descricao"]
            data.valor = values["valor"]
            data.data = DespesasModel.convert_params_by_datetime(values["data"])
            db.session.commit()
            return True
        except:
            return False
    
    
    @staticmethod
    def delete(id) -> bool:
        receita = DespesasModel.get(id)
        if receita is not None:
            db.session.delete(receita)
            db.session.commit()
            return True
        return False
        
    
    def __repr__(self) -> str:
        return "{}".format({
            "id": self.id,
            "categoria": self.categoria.value,
            "descrição": self.descricao,
            "valor": self.valor,
            "data": self.data
        })
    