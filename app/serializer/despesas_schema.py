from app.models.despesas_model import DespesasModel
from app.ext.flask_marshmallow import ma



class DespesasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DespesasModel
