from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail 
from eal_manager.config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

# initializes our Flask Application, creates a CSRF key to protect forms and
# initializes the sqlite database. 
# it will pull in from multiple Flask Blueprints

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from eal_manager.users.routes import users
    from eal_manager.main.routes import main
    from eal_manager.addresses.routes import addresses
    from eal_manager.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(addresses)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app



