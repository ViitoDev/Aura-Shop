from flask import Flask
from pymongo import MongoClient

db = None

def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    try:
        client = MongoClient(app.config['MONGO_URI'])
        app.db = client.get_default_database()
    except Exception as e:
        print(f'Error: error to connect to the database {e}')

    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    return app