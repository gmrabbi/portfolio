from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Optional, URL


class ProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    technologies = StringField('Technologies (comma-separated)', validators=[Optional()])
    github_link = StringField('GitHub Link', validators=[Optional(), URL()])
    demo_link = StringField('Demo Link', validators=[Optional(), URL()])
    image = FileField('Project Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    featured = BooleanField('Featured Project')
    submit = SubmitField('Save Project')