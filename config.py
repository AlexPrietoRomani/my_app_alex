# config.py
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_llave_secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'app.db')  # Configuración de SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva la función de seguimiento de modificaciones para ahorrar recursos
