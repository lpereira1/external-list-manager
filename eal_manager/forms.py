from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from eal_manager.models import User, IPAddress 
import ipaddress

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=40)])
    last_name = StringField('Last Name',
                           validators=[DataRequired(), Length(min=2, max=40)])
    email = StringField('Email', 
                        validators=[Email(message='INVALID'),DataRequired()])
    password = PasswordField('Password', 
                        validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user: 
            raise ValidationError('User already exists. Please choose another')
    
    

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
                                DataRequired(), 
                                Email()    ])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')

class CreateAddress(FlaskForm):
    address = StringField('Address', 
                            validators=[
                                DataRequired(),
                                Length(min=7, max=21) ])
    name = StringField('Description', validators=[ DataRequired(), Length(min=5, max=255)])
                                
    organization = StringField('Customer or Organization', validators=[ DataRequired(),
                                Length(min=2, max=140) ])
    creator_id = current_user
    
    submit = SubmitField('Create Address')

    def validate_address(self, addr):
        dup_ip = IPAddress.query.filter_by(address=addr.data).first()
        if dup_ip:
            raise ValidationError('Address already exists.')
        
        elif '/' in addr.data:
            try:
                ipaddress.ip_network(addr.data)
            except ValueError as e:
                if 'host bits set' in str(e):
                    raise ValidationError('You input a host IP with a mask for a network. Verify information')
                else:
                    raise ValidationError(e)
        else:
            try:
                ipaddress.ip_address(addr.data)
            except:
                raise ValidationError('Invalid CIDR address, please enter a valide CIDR network or host IP')



class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=40)])
    last_name = StringField('Last Name',
                           validators=[DataRequired(), Length(min=2, max=40)])
    email = StringField('Email', 
                        validators=[Email(message='INVALID'),DataRequired()])
    user_picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user: 
                raise ValidationError('User already exists. Please choose another')