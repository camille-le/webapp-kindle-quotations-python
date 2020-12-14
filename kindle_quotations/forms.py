from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField, RadioField


VALIDATION = "HTML/XML Only!"

class HTMLtoCSVForm(FlaskForm):
  filename = FileField(validators=[FileRequired(), FileAllowed(['xml', 'html'], VALIDATION)]) 
  submit1 = SubmitField('Download CSV')
    
    
class HTMLtoJSONForm(FlaskForm):    
  filename = FileField(validators=[FileRequired(), FileAllowed(['xml', 'html'], VALIDATION)]) 
  submit2 = SubmitField('Download JSON')

