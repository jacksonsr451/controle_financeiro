from marshmallow_enum import EnumField
from app.enum.categoria_enum import CategoriaEnum
from app.models.despesas_model import DespesasModel
from app.ext.flask_marshmallow import ma



class DespesasSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = DespesasModel
        fields = ('id', 'categoria', 'descricao', 'valor', 'data')

    
    id = ma.auto_field()
    categoria = EnumField(CategoriaEnum, by_value=True)
    descricao = ma.auto_field()
    valor = ma.auto_field()
    data = ma.auto_field(format='%Y-%m-%d %H:%M:%S')