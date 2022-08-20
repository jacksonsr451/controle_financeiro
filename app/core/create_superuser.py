from app.enum.roles_enum import RolesEnum
from app.models.users_model import UsersModel
from werkzeug.security import generate_password_hash
from app.ext.flask_sqlalchemy import db


class CreateSuperuser:
    def __init__(self, username, email, password) -> None:
        user = UsersModel(username=username, email=email, password=password)
        user.role = RolesEnum.SUPERUSER
        db.session.add(user)
        db.session.commit()