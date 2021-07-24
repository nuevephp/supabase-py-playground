from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, InputRequired, Length

class AuthForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired('Email is required.'), Email()])
    password = PasswordField('Password', validators=[InputRequired('Password is required.'), Length(min=6)])
