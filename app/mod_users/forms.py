from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(),DataRequired(message='Email address is required.')])
    password = PasswordField('Password', validators=[DataRequired(message='password is required')])