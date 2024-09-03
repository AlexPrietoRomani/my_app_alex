# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

# Instancia de las extensiones
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

# app/__init__.py (asegúrate de que está en el orden correcto)
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicialización de extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Registro de blueprints (importar después de crear la app)
    from app.views import auth, reports, models_creation, field_book, admin
    app.register_blueprint(auth.bp)
    app.register_blueprint(reports.bp)
    app.register_blueprint(models_creation.bp)
    app.register_blueprint(field_book.bp)
    app.register_blueprint(admin.bp)

    return app
