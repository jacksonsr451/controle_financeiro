from flask import Blueprint 
from flask_restful import Api


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)
# api.add_resource()

def init_app(app):
    app.register_blueprint(blueprint)
    