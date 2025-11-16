from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(min=2, max=50)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    message = TextAreaField(
        'Message',
        validators=[DataRequired(), Length(min=5)]
    )
    submit = SubmitField('Send')

from wtforms import PasswordField, BooleanField

class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=3, max=30)]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=4, max=10)]
    )

    remember = BooleanField("Remember me")

    submit = SubmitField("Log in")
