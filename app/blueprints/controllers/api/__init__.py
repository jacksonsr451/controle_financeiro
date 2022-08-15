from flask import Blueprint 
from flask_restful import Api
from .despesas import Despesas, DespesasByAnoEMes, DespesasByID

from .receitas import Receitas, ReceitaByID, ReceitasByAnoEMes
from .resumo import Resumo

from .users import Users


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_resource(Receitas, "/receitas")
api.add_resource(ReceitaByID, "/receitas/<id>")
api.add_resource(Despesas, "/despesas")
api.add_resource(DespesasByID, "/despesas/<id>")
api.add_resource(DespesasByAnoEMes, "/despesas/<ano>/<mes>")
api.add_resource(ReceitasByAnoEMes, "/receitas/<ano>/<mes>")
api.add_resource(Resumo, "/resumo/<ano>/<mes>")
api.add_resource(Users, "/usuarios")


def init_app(app):
    app.register_blueprint(blueprint)
    