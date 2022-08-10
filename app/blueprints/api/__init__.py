from flask import Blueprint 
from flask_restful import Api
from app.blueprints.api.despesas import Despesas, DespesasByAnoEMes, DespesasByID

from app.blueprints.api.receita import Receita, ReceitaByID, ReceitasByAnoEMes
from app.blueprints.api.resumo import Resumo


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)
api.add_resource(Receita, "/receitas")
api.add_resource(ReceitaByID, "/receitas/<id>")
api.add_resource(Despesas, "/despesas")
api.add_resource(DespesasByID, "/despesas/<id>")
api.add_resource(DespesasByAnoEMes, "/despesas/<ano>/<mes>")
api.add_resource(ReceitasByAnoEMes, "/receitas/<ano>/<mes>")
api.add_resource(Resumo, "/resumo/<ano>/<mes>")


def init_app(app):
    app.register_blueprint(blueprint)
    