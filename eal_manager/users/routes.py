from PIL import Image
from flask import render_template, flash, redirect, url_for, request, Blueprint
from eal_manager.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from eal_manager.models import User
from eal_manager import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required


users = Blueprint('users', __name__)

@users.route("/register", methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.startpage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name = form.first_name.data, last_name= form.last_name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/login",methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.startpage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.startpage'))
        else:
            flash('Login Unsuccessful', 'danger')

    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    
    return redirect(url_for('main.startpage'))

@users.route("/account", methods=['POST', 'GET'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.user_picture.data: 
            picture_file = save_picture(form.user_picture.data)
            current_user.image_file = picture_file
        current_user.email = form.email.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.email.data = current_user.email
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
    image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@users.route("/requestreset/", methods=['POST', 'GET'])
def request_reset():
    if current_user.is_authenticated:
        return redirect(url_for('main.startpage'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route("/requestreset/<token>", methods=['POST', 'GET'])
def password_reset(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.startpage'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is invalid or expired Token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Password Reset successfully for {user.email}!', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_password.html', title='Reset Password', form=form)

