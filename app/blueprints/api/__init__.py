from flask import Blueprint 
from flask_restful import Api

from app.blueprints.api.receita import Receita, ReceitaByID


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)
api.add_resource(Receita, "/receitas")
api.add_resource(ReceitaByID, "/receitas/<id>")


def init_app(app):
    app.register_blueprint(blueprint)
    