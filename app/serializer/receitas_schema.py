from app.models.receitas_model import ReceitasModel
from app.ext.flask_marshmallow import ma



class ReceitasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ReceitasModel
        # exclude = ['id']
