from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, CreateAddress, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 


# initializes our Flask Application, creates a CSRF key to protect forms and
# initializes the sqlite database. 

app = Flask(__name__)
app.config['SECRET_KEY'] = '089uyt8654dvb543giklu8!o.76453swd2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///addresses.db'
db = SQLAlchemy(app)

# Creates Database Columns based on Models. There are user who create address and 
# those addresses are part of an organization.
# user_1 = User(email='l@l.com', password = 'test')
# UNIQUE constraint failed: user.image_file
# user_2 = User(email='lazaro.pereira@gmail.com', password='Lazaro1')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(140), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    addresses = db.relationship('IPAddress', backref='creator', lazy=True)

    def __repr__(self):
        return f'User("{self.email}", "{self.image_file}")'

class IPAddress(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(20)) 
    name = db.Column(db.String(255))
    organization = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False )
    
    def __repr__(self):
        return f'User("{self.address}","{self.name}", "{self.organization}", "{self.date_created})'



whitelisted_addresses=[ 
    { 'name': 'ip1',
    'organization':'bobs burgers',
    'address': '10.10.10.10/32'
    },
    { 'name' : 'ip2',
    'organization': 'bobs burgers',
    'address': '10.10.10.20/32'
    },
    { 'name': 'ip3',
    'organization':'bobs burgers',
    'address': '10.10.10.30/32'
    },
]


@app.route("/")
def startpage():
    return render_template('index.html', whitelisted_addresses=whitelisted_addresses)

@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('startpage'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login",methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@laz.com' and form.password.data == 'Lazaro1':
            flash('Successful logon', 'success')
            return redirect(url_for('startpage'))
        else:
            flash('Login Unsuccessful', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route("/create/address", methods=['POST', 'GET'])
def createaddress():
    form = CreateAddress()
    if form.is_submitted():
        flash(f'Account created for {form.address.data}!', 'success')
    return render_template('createaddress.html', title='Create Address', form=form)


if __name__ == '__main__':
    app.run(debug=True)
