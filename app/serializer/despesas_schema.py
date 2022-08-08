from marshmallow_enum import EnumField

from app.models.despesas_model import CategoriaEnum, DespesasModel
from app.ext.flask_marshmallow import ma



class DespesasSchema(ma.SQLAlchemyAutoSchema):
    categoria = EnumField(CategoriaEnum, by_value=True)
    
    
    class Meta:
        model = DespesasModel
