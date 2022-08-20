from marshmallow_enum import EnumField
from app.models.users_model import UsersModel
from app.ext.flask_marshmallow import ma


class UsersSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, data=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = self.dump(data)

    class Meta:
        model = UsersModel
        fields = ('id', 'username', 'email')

    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
