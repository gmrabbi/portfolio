from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Optional


class LeadershipForm(FlaskForm):
    title = StringField('Activity Title', validators=[DataRequired()])
    organization = StringField('Organization', validators=[DataRequired()])
    role = StringField('Role', validators=[Optional()])
    description = TextAreaField('Description', validators=[Optional()])
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[Optional()])
    current = BooleanField('Currently Active')
    submit = SubmitField('Save Activity')