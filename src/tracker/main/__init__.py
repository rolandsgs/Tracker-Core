from flask import Blueprint
           
bp = Blueprint('main', __name__)
           
from tracker.main import routes