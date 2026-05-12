from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, Optional, URL


class ProfileForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    title = StringField('Professional Title', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[Optional()])
    location = StringField('Location', validators=[Optional()])
    years_of_experience = IntegerField('Years of Experience', validators=[Optional(), NumberRange(min=0, max=100)])
    github = StringField('GitHub URL', validators=[Optional(), URL()])
    linkedin = StringField('LinkedIn URL', validators=[Optional(), URL()])
    kaggle = StringField('Kaggle URL', validators=[Optional(), URL()])
    scholar = StringField('Google Scholar URL', validators=[Optional(), URL()])
    school = StringField('High School', validators=[Optional()])
    college = StringField('College', validators=[Optional()])
    university = StringField('University', validators=[Optional()])
    about = TextAreaField('About', validators=[DataRequired()])
    submit = SubmitField('Update Profile')