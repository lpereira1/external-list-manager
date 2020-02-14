import secrets
from PIL import Image
import os
from flask import render_template, flash, redirect, url_for, request
from eal_manager.forms import RegistrationForm, CreateAddress, LoginForm, UpdateAccountForm
from eal_manager.models import User, IPAddress
from eal_manager import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required



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

@app.route("/address/<int:addr_id>", methods=['POST', 'GET'])
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
