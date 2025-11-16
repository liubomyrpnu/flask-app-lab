from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, Regexp

class ContactForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            DataRequired(),
            Length(min=4, max=10, message="Name must be 4–10 characters")
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Invalid email")
        ]
    )

    phone = StringField(
        "Phone",
        validators=[
            DataRequired(),
            Regexp(
                r'^\+380\d{9}$',
                message="Phone must match +380XXXXXXXXX"
            )
        ]
    )

    subject = SelectField(
        "Subject",
        choices=[
            ("support", "Technical support"),
            ("order", "Order question"),
            ("feedback", "Feedback"),
            ("other", "Other")
        ],
        validators=[DataRequired()]
    )

    message = TextAreaField(
        "Message",
        validators=[
            DataRequired(),
            Length(max=500, message="Message must be <= 500 characters")
        ]
    )

    submit = SubmitField("Send")

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
