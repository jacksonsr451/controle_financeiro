from marshmallow_enum import EnumField

from app.enum.categoria_enum import CategoriaEnum
from app.ext.flask_marshmallow import ma
from app.models.despesas_model import DespesasModel


class DespesasSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, data=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = self.dump(data)

    class Meta:
        model = DespesasModel
        fields = ('id', 'categoria', 'descricao', 'valor', 'data')

    id = ma.auto_field()
    categoria = EnumField(CategoriaEnum, by_value=True)
    descricao = ma.auto_field()
    valor = ma.auto_field()
    data = ma.auto_field(format='%Y-%m-%d %H:%M:%S')
