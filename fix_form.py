#!/usr/bin/env python
# Temporary fix script for profile_form.py
content = '''from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, Optional, URL, ValidationError
from app.models.user import User


class ProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Full Name', validators=[DataRequired()])
    title = StringField('Professional Title', validators=[DataRequired()])
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
    password = PasswordField('New Password (leave empty to keep current)', validators=[Optional(), Length(min=6)])
    password_confirm = PasswordField('Confirm Password', validators=[Optional(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Update Profile')

    def validate_username(self, field):
        existing_user = User.query.filter_by(username=field.data).first()
        if existing_user and existing_user.id != getattr(self, '_user_id', None):
            raise ValidationError('Username already taken.')

    def validate_email(self, field):
        existing_user = User.query.filter_by(email=field.data).first()
        if existing_user and existing_user.id != getattr(self, '_user_id', None):
            raise ValidationError('Email already taken.')
'''

with open('app/forms/profile_form.py', 'w') as f:
    f.write(content)
print('Profile form fixed successfully!')
