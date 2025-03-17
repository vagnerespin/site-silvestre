
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sua_chave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)
    login_manager.init_app(app)

    # Registrar current_user nos templates
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)

    # Importar e registrar Blueprints
    from .views import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
