from flask import Flask

from tracker.database import DB
from tracker.models.user import User
from tracker.main import bp as main_bp


def create_app():
    
    DB.init()
    register_blueprints(app)
    return app

def register_blueprints(app):
    app.register_blueprint(main_bp)

app = Flask(__name__)
create_app()