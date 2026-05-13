from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, FloatField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Optional, NumberRange


class EducationForm(FlaskForm):
    institution = StringField('Institution', validators=[DataRequired()])
    degree = StringField('Degree', validators=[DataRequired()])
    field_of_study = StringField('Field of Study', validators=[DataRequired()])
    start_date = DateField('Start Date', validators=[Optional()])
    end_date = DateField('End Date', validators=[Optional()])
    cgpa = FloatField('CGPA/GPA', validators=[Optional(), NumberRange(min=0, max=5)])
    cgpa_scale = StringField('CGPA Scale', validators=[Optional()])
    description = TextAreaField('Description', validators=[Optional()])
    current = BooleanField('Currently Studying')
    order = IntegerField('Display Order', validators=[Optional()], default=0)
    submit = SubmitField('Save Education')