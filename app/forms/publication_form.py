from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional, URL


class PublicationForm(FlaskForm):
    title = StringField('Publication Title', validators=[DataRequired()])
    journal = StringField('Journal/Conference', validators=[DataRequired()])
    authors = StringField('Authors', validators=[Optional()])
    link = StringField('Publication Link', validators=[Optional(), URL()])
    status = SelectField('Status', choices=[
        ('Published', 'Published'),
        ('In Review', 'In Review'),
        ('Accepted', 'Accepted'),
        ('Submitted', 'Submitted')
    ], validators=[DataRequired()])
    publication_date = DateField('Publication Date', validators=[Optional()])
    image = FileField('Publication Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Save Publication')