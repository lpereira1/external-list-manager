from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


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

from eal_manager import routes