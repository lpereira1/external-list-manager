from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from eal_manager.models import User 

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
        elif 'abrigo.com' not in email.data:
            raise ValidationError('User must be an abrigo.com username to be able to access this system')

    
    

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
                                DataRequired(), 
                                Email()    ])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')



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


class RequestResetForm(FlaskForm):
    email = StringField('Email', 
                        validators=[Email(message='INVALID'),DataRequired()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None: 
            raise ValidationError('No Account exists with this email. Please register first')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', 
                        validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')