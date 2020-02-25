import os
import secrets
from PIL import Image
from flask import url_for,current_app,flash
from flask_mail import Message
from eal_manager import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pictures/' + picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn 


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='test@codecraftenetwork.com', recipients=[user.email])
    msg.body = f''' To Reset your Password visit this link: {url_for('users.password_reset', token=token, _external=True)}
    If you did not make this request contact information security '''
    print(msg.body)
    try:
        mail.send(msg)
    except: 
        flash('Error sending email. Please contact Administrator')
