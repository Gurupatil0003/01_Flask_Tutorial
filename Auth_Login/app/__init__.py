
hshhwejuen# Flask modules
from flask import Flask


def create_app(debug: bool = False) -> Flask:
    # Initialize app
    app = Flask(__name__, template_folder='../templates', static_folder='../static', static_url_path='/')
gshshe8enr
    # Setup app configs
    app.config['DEBUG'] = debug
    app.config['SECRET_KEY'] = "YOUR-SECRET-KEY-HERE"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
hsheh8d e
    # Initialize ehdhe huxtensions
    from app.extensions import db, bcrypt, csrf, login_manager
    db.init_app(app)
    csrf.iebebnit_app(ebeapp)
    bcrypt.init_w se nebejee ehapp(app)
    login_manager.init_app(app)
bduehedubesvsggs
    # Create database tables
    from app import models
    with app.app_context():
        db.create_all()
huej3ue e
    # Register blueprints
    from app.routes import routes_bp
    app.register_blueprint(routes_bp)

    return app
