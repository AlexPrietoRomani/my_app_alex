# app/models.py
from app import db  # Importación correcta desde app
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # Ej: 'evaluador', 'moderador', 'admin'

class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    fields = db.relationship('Field', backref='template', lazy=True)

class Field(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template_id = db.Column(db.Integer, db.ForeignKey('template.id'), nullable=False)
    field_type = db.Column(db.String(50), nullable=False)  # e.g., 'text', 'number', 'image', etc.
    label = db.Column(db.String(100), nullable=False)
    required = db.Column(db.Boolean, default=False)

class FieldBookEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    data = db.Column(db.JSON)  # Almacenar datos como JSON
