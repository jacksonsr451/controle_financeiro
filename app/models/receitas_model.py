from flask_jwt_extended import get_jwt_identity
from datetime import datetime
from app.ext.flask_sqlalchemy import db
from app.models.users_model import UsersModel


class ReceitasModel(db.Model):
    __tablename__ = 'receitas'
    __table_args__ = (
        db.UniqueConstraint(
            'descricao', 'data', name='unique_descricao_for_data'
        ),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    descricao = db.Column(db.Text, nullable=False)
    valor = db.Column(db.String(50), nullable=False)
    data = db.Column(db.DateTime, nullable=False)

    def __init__(self, descricao, valor, data) -> None:
        self.descricao = descricao
        self.valor = valor
        self.data = self.convert_params_by_datetime(data)

    @classmethod
    def add_user_id(cls, user_id):
        cls.user_id = user_id
        return cls

    @staticmethod
    def convert_params_by_datetime(value) -> datetime:
        if type(value) is str:
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        return ReceitasModel.convert_params_by_datetime(
            value.strftime('%Y-%m-%d %H:%M:%S')
        )

    @staticmethod
    def filter_by_descicao(descricao) -> list:
        user = UsersModel.get_user_by_email(email=get_jwt_identity()['email'])
        return (
            ReceitasModel.query.filter(ReceitasModel.user_id == user.id)
            .filter(ReceitasModel.descricao.like('%{}%'.format(descricao)))
            .all()
        )

    @staticmethod
    def filter_by_ano_and_mes(ano, mes) -> list:
        user = UsersModel.get_user_by_email(email=get_jwt_identity()['email'])
        return (
            ReceitasModel.query.filter(ReceitasModel.user_id == user.id)
            .filter(ReceitasModel.data.like('%{}-{}%'.format(ano, mes)))
            .all()
        )

    @staticmethod
    def all() -> list:
        return ReceitasModel.query.all()

    @staticmethod
    def add(request) -> bool:
        try:
            new_receita = ReceitasModel(
                descricao=request['descricao'],
                valor=request['valor'],
                data=request['data'],
            )
            db.session.add(new_receita)
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def get(id) -> dict:
        user = UsersModel.get_user_by_email(email=get_jwt_identity()['email'])
        return (
            ReceitasModel.query.filter(ReceitasModel.user_id == user.id)
            .filter_by(id=id)
            .first()
        )

    @staticmethod
    def put(id, values) -> bool:
        try:
            data = ReceitasModel.get(id)
            data.descricao = values['descricao']
            data.valor = values['valor']
            data.data = ReceitasModel.convert_params_by_datetime(
                values['data']
            )
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def delete(id) -> bool:
        user = UsersModel.get_user_by_email(email=get_jwt_identity()['email'])
        receita = (
            ReceitasModel.query.filter(ReceitasModel.user_id == user.id)
            .filter_by(id=id)
            .first()
        )
        if receita is not None:
            db.session.delete(receita)
            db.session.commit()
            return True
        return False

    def __repr__(self) -> str:
        return '{}'.format(
            {
                'id': self.id,
                'descrição': self.descricao,
                'valor': self.valor,
                'data': self.data,
            }
        )
