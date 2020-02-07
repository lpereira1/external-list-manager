from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField,ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    email = StringField('Email', 
                        validators=[Email(message='INVALID'),DataRequired()])
    password = PasswordField('Password', 
                        validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password', 
                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

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