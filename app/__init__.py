from flask import Flask
from .routes.main import main as main_blueprint
from .errors.handlers import errors as errors_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    app.register_blueprint(main_blueprint)
    app.register_blueprint(errors_blueprint)

    return app
