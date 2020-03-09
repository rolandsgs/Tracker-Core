from flask import render_template
        
from tracker.main import bp
from tracker.main.controller import list_active_sessions
from tracker.main.controller import get_data_by_username
from tracker.main.controller import how_many_access_by_labs
from tracker.main.controller import how_many_users_active
from tracker.models.user import User
from tracker.database import DB

@bp.route('/')
def index():
    users_front = list_active_sessions()
    length = how_many_users_active()
    return render_template('index.html', lista_users=users_front,active=length)

@bp.route('/grafico')
def chart():
    access_by_dates = how_many_access_by_labs()
    return render_template('grafico.html', datas=access_by_dates)

@bp.route('/user/<username>')
def get_user(username):
    user = get_data_by_username(username)
    return render_template('usuario.html', user=user)

