from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired 
from wtforms.validators import DataRequired 
from wtforms import SubmitField


class HTMLtoCSVForm(FlaskForm):
    filename = FileField(validators=[FileRequired()]) 
    submit = SubmitField('Download CSV')


