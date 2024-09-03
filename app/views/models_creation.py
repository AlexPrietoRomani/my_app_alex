# app/views/models_creation.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.models import db, Template, Field

bp = Blueprint('models_creation', __name__, url_prefix='/models')

@bp.route('/', methods=['GET', 'POST'])
@login_required
def create_model():
    if current_user.role not in ['moderador', 'admin']:
        return redirect(url_for('reports.view_reports'))
    
    if request.method == 'POST':
        template_name = request.form['name']
        new_template = Template(name=template_name)
        db.session.add(new_template)
        db.session.commit()
        # Aquí podrías agregar lógica para agregar campos a la plantilla
        return redirect(url_for('models_creation.create_model'))
    templates = Template.query.all()
    return render_template('create_model.html', templates=templates)
