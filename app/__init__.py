from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager 
from flask_bootstrap import Bootstrap 


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_message = "Você deve fazer login para acessar esta página"
login.login_view = "auth.login"
bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)

    from app.admin import admin as admin_blueprint

    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    from app.auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    from app.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app