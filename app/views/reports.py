# app/views/reports.py
from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('reports', __name__, url_prefix='/reports')

@bp.route('/')
def view_reports():
    # Lógica básica para mostrar la vista de reportes
    return render_template('report.html', reports=[])

