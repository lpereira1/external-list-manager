import secrets
from PIL import Image
import os
from flask import render_template, flash, redirect, url_for, request
from eal_manager.forms import RegistrationForm, CreateAddress, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from eal_manager.models import User, IPAddress
from eal_manager import app, db, bcrypt , mail
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message



@app.route("/")
@login_required
def startpage():
    page = request.args.get('page', 1, type=int)
    whitelisted_addresses = IPAddress.query.order_by(IPAddress.date_created.desc()).paginate(page=page, per_page=20)
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

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pictures/' + picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn 


@app.route("/account", methods=['POST', 'GET'])
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
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.email.data = current_user.email
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
    image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)



@app.route("/address", methods=['POST', 'GET'])
@login_required
def createaddress():
    form = CreateAddress()
    form.submit.label.text = 'Create Address'
    if form.validate_on_submit():
        address = IPAddress(address= form.address.data, 
                            name= form.name.data, 
                            organization=form.organization.data,
                            creator_id = current_user.first_name + ' ' + current_user.last_name )
        db.session.add(address)
        db.session.commit()
        flash(f'Whitelist updated with {form.address.data}!', 'success')
    return render_template('createaddress.html', title='startpage', form=form, legend='Create a new Address')

@login_required
def addr(addr_id):
    address = IPAddress.query.get_or_404(addr_id)
    return render_template('address.html', title='addr.address', address=address)


@app.route("/address/<int:addr_id>/update", methods=['POST', 'GET'])
@login_required
def update_addr(addr_id):
    address = IPAddress.query.get_or_404(addr_id)
    # Eventually we need to add a read and read/write permission here like
    # if address.creator_id.permissions != Write:
    #     abort(403)
    form = CreateAddress()
    form.submit.label.text = 'Update Address'

    
    if form.validate_on_submit():
        address.address = form.address.data
        address.name = form.name.data
        address.organization = form.organization.data
        address.creator_id = current_user.first_name + ' ' + current_user.last_name
        db.session.commit()
        flash('Address updated' , 'success')
        return redirect(url_for('startpage'))
    elif request.method == 'GET':
        form.address.data = address.address
        form.name.data = address.name
        form.organization.data = address.organization
        return render_template('createaddress.html', title='Update Address', 
                            form=form, legend='Update Address')

@app.route("/address/<int:addr_id>/delete", methods=['POST'])
@login_required
def delete_addr(addr_id):
    address = IPAddress.query.get_or_404(addr_id)
    db.session.delete(address)
    db.session.commit()
    flash('Address Deleted' , 'success')
    return redirect(url_for('startpage'))

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='test@codecraftenetwork.com', recipients=[user.email])
    msg.body = f''' To Reset your Password visit this link: {url_for('password_reset', token=token, _external=True)}
    If you did not make this request contact information security '''
    print(msg.body)
    try:
        mail.send(msg)
    except: 
        flash('Error sending email. Please contact Administrator')


@app.route("/requestreset/", methods=['POST', 'GET'])
def request_reset():
    if current_user.is_authenticated:
        return redirect(url_for('startpage'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/requestreset/<token>", methods=['POST', 'GET'])
def password_reset(token):
    if current_user.is_authenticated:
        return redirect(url_for('startpage'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is invalid or expired Token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Password Reset successfully for {user.email}!', 'success')
        return redirect(url_for('login'))
    return render_template('reset_password.html', title='Reset Password', form=form)




