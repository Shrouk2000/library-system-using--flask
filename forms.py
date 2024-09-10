# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=120)])
    cover_photo = FileField('Cover Photo')
    number_of_pages = IntegerField('Number of Pages', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
