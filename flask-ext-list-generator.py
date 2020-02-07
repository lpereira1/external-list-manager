from flask import Flask, render_template
from forms import RegistrationForm, CreateAddress, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '089uyt8654dvb543giklu8!o.76453swd2'


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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route("/create/address")
def createaddress():
    form = CreateAddress()
    return render_template('createaddress.html', title='Create Address', form=form)


if __name__ == '__main__':
    app.run(debug=True)
