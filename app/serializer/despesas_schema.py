from marshmallow_enum import EnumField
from app.enum.categoria_enum import CategoriaEnum
from app.models.despesas_model import DespesasModel
from app.ext.flask_marshmallow import ma



class DespesasSchema(ma.SQLAlchemyAutoSchema):
    categoria = EnumField(CategoriaEnum, by_value=True)
    
    
    class Meta:
        model = DespesasModel
