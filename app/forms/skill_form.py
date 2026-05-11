from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange


class SkillForm(FlaskForm):
    category = SelectField('Category', choices=[
        ('Machine Learning', 'Machine Learning'),
        ('Deep Learning', 'Deep Learning'),
        ('Computer Vision', 'Computer Vision'),
        ('IoT', 'IoT'),
        ('Web Development', 'Web Development'),
        ('Research', 'Research'),
        ('Tools', 'Tools')
    ], validators=[DataRequired()])
    name = StringField('Skill Name', validators=[DataRequired()])
    proficiency = IntegerField('Proficiency (1-100)', validators=[DataRequired(), NumberRange(min=1, max=100)])
    submit = SubmitField('Save Skill')