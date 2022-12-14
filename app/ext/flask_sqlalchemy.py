from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app, **config):
    from app import models

    db.init_app(app=app, **config)
