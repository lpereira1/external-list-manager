from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# initializes our Flask Application, creates a CSRF key to protect forms and
# initializes the sqlite database. 
# it will pull in from routes.py, and forms.py

app = Flask(__name__)
app.config['SECRET_KEY'] = '089uyt8654dvb543giklu8!o.76453swd2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///addresses.db'
db = SQLAlchemy(app)

from eal_manager import routes