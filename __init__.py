from flask import Flask
from config import Config
from routes import routes  
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register the blueprint
    app.register_blueprint(routes)

    return app
