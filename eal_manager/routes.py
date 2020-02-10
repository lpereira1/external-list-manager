from flask import render_template, flash, redirect, url_for, request
from eal_manager.forms import RegistrationForm, CreateAddress, LoginForm
from eal_manager.models import User, IPAddress
from eal_manager import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required


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
    if current_user.is_authenticated:
        return redirect(url_for('startpage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name = form.first_name.data, last_name= form.last_name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login",methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('startpage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('startpage'))
        else:
            flash('Login Unsuccessful', 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('startpage'))


@app.route("/account")
@login_required
def account():
    image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file)



@app.route("/create/address", methods=['POST', 'GET'])
def createaddress():
    form = CreateAddress()
    if form.is_submitted():
        flash(f'Account created for {form.address.data}!', 'success')
    return render_template('createaddress.html', title='Create Address', form=form)