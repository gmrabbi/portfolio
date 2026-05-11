from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Optional, URL


class CertificationForm(FlaskForm):
    title = StringField('Certification Title', validators=[DataRequired()])
    issuer = StringField('Issuing Organization', validators=[DataRequired()])
    issue_date = DateField('Issue Date', validators=[DataRequired()])
    expiry_date = DateField('Expiry Date', validators=[Optional()])
    credential_id = StringField('Credential ID', validators=[Optional()])
    credential_url = StringField('Credential URL', validators=[Optional(), URL()])
    submit = SubmitField('Save Certification')