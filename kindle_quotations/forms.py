from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed 
from wtforms import SubmitField



class HTMLtoCSVForm(FlaskForm):
    filename = FileField(validators=[FileRequired(), FileAllowed(['xml', 'html'], "HTML/XML Only!")]) 
    submit1 = SubmitField('Download CSV')
    
class HTMLtoJSONForm(FlaskForm):    
    filename = FileField(validators=[FileRequired(), FileAllowed(['xml', 'html'], "HTML/XML Only!")]) 
    submit2 = SubmitField('Download JSON')



