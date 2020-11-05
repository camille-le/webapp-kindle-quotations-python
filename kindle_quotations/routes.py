import os 
import random
from flask import render_template, url_for, flash, redirect, request, send_from_directory, make_response, jsonify
from werkzeug.utils import secure_filename
from kindle_quotations import app 
from kindle_quotations.models import process
from kindle_quotations.forms import HTMLtoCSVForm, HTMLtoJSONForm
import io; io.StringIO()
import json


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
HOME = 'home.html'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 # 1 MB


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
        upload_file = csv_form.filename.data # FileStore object         
        fname = secure_filename(upload_file.filename) 
        upload_file.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))
        return download_csv(fname)      
    return render_template(HOME, csv_form=csv_form, json_form=json_form)                        
    
@app.route('/htmljson', methods=['POST'])
def htmljson(): 
    csv_form = HTMLtoCSVForm() 
    json_form = HTMLtoJSONForm() 
    if json_form.validate_on_submit(): 
        upload_file = csv_form.filename.data # FileStore object         
        fname = secure_filename(upload_file.filename) 
        upload_file.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))
        return download_json(fname)
    return render_template(HOME, csv_form=csv_form, json_form=json_form)    


@app.route('/uploads/<filename>')
def uploaded_file(filename):       
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


@app.route('/contact') 
def contact(): 
    return render_template('contact.html')


def download_json(filename): 
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)     
    data = process(filepath, 'json') # returns a list of dict      
    content_disposition = "attachment; filename="
    content_disposition += filename + ".json"
    response = make_response(json.dumps(data, indent=2)) 
    response.headers["Content-Disposition"] = content_disposition
    response.mimetype = 'application/json'
    os.remove(filepath)        
    return response
        

def download_csv(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)     
    data = process(filepath, 'csv') # returns a string with newlines     
    output = io.StringIO() 
    output.write(data)    
    os.remove(filepath)        
    # Write StringIO file contents to a response with CSV format 
    response = make_response(output.getvalue()) 
    content_disposition = "attachment; filename="
    content_disposition += filename.split(".")[0] + ".csv"
    response.headers["Content-Disposition"] = content_disposition
    response.headers["Content-type"] = "text/csv"
    response.mimetype='text/csv'
    return response        


