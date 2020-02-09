from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, CreateAddress, LoginForm
from flask_sqlalchemy import SQLAlchemy
from models import User, IPAddress

# initializes our Flask Application, creates a CSRF key to protect forms and
# initializes the sqlite database. 

app = Flask(__name__)
app.config['SECRET_KEY'] = '089uyt8654dvb543giklu8!o.76453swd2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///addresses.db'
db = SQLAlchemy(app)





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
