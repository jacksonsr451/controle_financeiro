from dynaconf import FlaskDynaconf


def init_app(app, **configs):
    FlaskDynaconf(app=app, **configs)
