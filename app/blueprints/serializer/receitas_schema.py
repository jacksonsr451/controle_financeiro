from app.models.receitas_model import ReceitasModel
from app.ext.flask_marshmallow import ma


class ReceitasSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, data=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = self.dump(data)

    class Meta:
        model = ReceitasModel
        fields = ('id', 'descricao', 'valor', 'data')

    id = ma.auto_field()
    descricao = ma.auto_field()
    valor = ma.auto_field()
    data = ma.auto_field(format='%Y-%m-%d %H:%M:%S')
