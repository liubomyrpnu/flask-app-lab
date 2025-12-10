from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired(), Length(max=150)])
    content = TextAreaField('Зміст', validators=[DataRequired()])
    category = StringField('Категорія', default="Без категорії")
    submit = SubmitField('Зберегти')