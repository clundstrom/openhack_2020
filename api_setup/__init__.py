from src.routes.open import open_routes
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from environs import Env
import os


def create_api():
    """
    This function sets up the API based on configurations
    specified by api.env
    :return: app
    """

    app = Flask(__name__)
    env = Env()
    api = Api()

    # Read env file into os
    env.read_env('api_setup/api.env')

    # Read settings to connect to DB
    app.config['MYSQL_HOST'] = 'db' if os.environ.get('RUN_IN_CONTAINER')==1 else os.environ.get('MYSQL_HOST')
    app.config['MYSQL_DATABASE'] = os.environ.get('MYSQL_DATABASE')
    app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
    app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
    app.config['MYSQL_PORT'] = os.environ.get('MYSQL_PORT')
    app.config['DEBUG'] = os.environ.get('DEBUG')

    # Setup RESTFUL and CORS
    api.init_app(app)
    CORS(app)

    # Register Blueprints
    app.register_blueprint(open_routes, url_prefix='/api/v1')

    return app