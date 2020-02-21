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
<<<<<<< HEAD
# it will pull in from routes.py, and forms.py

app = Flask(__name__)
app.config['SECRET_KEY'] = '089uyt8654dvb543giklu8!o.76453swd2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///addresses.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from eal_manager.users.routes import users
from eal_manager.main.routes import main
from eal_manager.addresses.routes import addresses

app.register_blueprint(users)
app.register_blueprint(addresses)
app.register_blueprint(main)
=======
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



>>>>>>> d740a5a02b57b29eba7a45bc1b89a421ca9f126a
