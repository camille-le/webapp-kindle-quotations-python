import json, os, random, io; io.StringIO()
from flask import render_template, flash, send_from_directory, make_response 
from werkzeug.utils import secure_filename
from kindle_quotations import app 
from kindle_quotations.models import process_csv, process_json, download_csv, download_json
from kindle_quotations.forms import HTMLtoCSVForm, HTMLtoJSONForm


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
HOME = 'home.html'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 0.5 * 1024 * 1024 # 500 KB


@app.route("/")
def home(): 
    csv_form = HTMLtoCSVForm() 
    json_form = HTMLtoJSONForm() 
    return render_template(HOME, csv_form=csv_form, json_form=json_form)


@app.route('/csv', methods=['POST'])
def csv(): 
    csv_form = HTMLtoCSVForm() 
    json_form = HTMLtoJSONForm() 
    if csv_form.validate_on_submit(): 
        upload_file = csv_form.filename.data # <class 'werkzeug.datastructures.FileStorage'>        
        upload_file = upload_file.read().decode("utf-8") # <class 'bytes'>           
        output = io.StringIO() 
        output.write(upload_file) # string of XML representation                  
        return download_csv(upload_file)    
    return render_template(HOME, csv_form=csv_form, json_form=json_form)                        
    

@app.route('/htmljson', methods=['POST'])
def htmljson(): 
    csv_form = HTMLtoCSVForm() 
    json_form = HTMLtoJSONForm() 
    if json_form.validate_on_submit(): 
        upload_file = csv_form.filename.data 
        upload_file = upload_file.read().decode("utf-8")
        output = io.StringIO() 
        output.write(upload_file) 
        return download_json(upload_file) 
    return render_template(HOME, csv_form=csv_form, json_form=json_form)    


@app.route('/uploads/<filename>')
def uploaded_file(filename):       
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


@app.route('/contact') 
def contact(): 
    return render_template('contact.html')




