import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail 



# initializes our Flask Application, creates a CSRF key to protect forms and
# initializes the sqlite database. 
# it will pull in from routes.py, and forms.py

app = Flask(__name__)
app.config['SECRET_KEY'] = '089uyt8654dvb543giklu8!o.76453swd2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///addresses.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
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
