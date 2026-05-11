from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Optional, URL


class ProfileForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    title = StringField('Professional Title', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[Optional()])
    location = StringField('Location', validators=[Optional()])
    github = StringField('GitHub URL', validators=[Optional(), URL()])
    linkedin = StringField('LinkedIn URL', validators=[Optional(), URL()])
    kaggle = StringField('Kaggle URL', validators=[Optional(), URL()])
    scholar = StringField('Google Scholar URL', validators=[Optional(), URL()])
    about = TextAreaField('About', validators=[DataRequired()])
    submit = SubmitField('Update Profile')