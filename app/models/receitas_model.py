from app.ext.flask_sqlalchemy import db



class ReceitasModel(db.Model):
    __tablename__ = "receitas"
    
    id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.Text, nullable=False)
    valor = db.Column(db.String(50), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    
    
    def __init__(self, id, descricao, valor, data) -> None:
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.data = data
        
    
    def __repr__(self) -> str:
        return "{}".format({
            "id": self.id,
            "descrição": self.descricao,
            "valor": self.valor,
            "data": self.data
        })
    