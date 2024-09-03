# app/views/field_book.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.models import db, FieldBookEntry

bp = Blueprint('field_book', __name__, url_prefix='/field_book')

@bp.route('/', methods=['GET', 'POST'])
@login_required
def manage_field_book():
    if current_user.role not in ['moderador', 'admin']:
        return redirect(url_for('reports.view_reports'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_entry = FieldBookEntry(title=title, description=description, data={})
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('field_book.manage_field_book'))
    entries = FieldBookEntry.query.all()
    return render_template('field_book.html', entries=entries)
