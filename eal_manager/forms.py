from flask_wtf import FlaskForm
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
    
    

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
                                DataRequired(), 
                                Email()    ])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')

class CreateAddress(FlaskForm):
    address = StringField('Username', 
                            validators=[
                                DataRequired(),
                                Length(min=2, max=20) ])
    description = StringField('Email', validators=[
                                DataRequired(), 
                                Email()    ])
    organization = StringField('Username', 
                            validators=[
                                DataRequired(),
                                Length(min=2, max=20) ])
    submit = SubmitField('Sign Up')