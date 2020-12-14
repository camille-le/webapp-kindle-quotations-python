import json, os, random, io; io.StringIO()
from flask import render_template, request  
from werkzeug.utils import secure_filename
from kindle_quotations import app 
from kindle_quotations.models import download_csv, download_json 
from kindle_quotations.forms import HTMLtoCSVForm, HTMLtoJSONForm


HOME = 'home.html'

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
        upload_file = upload_file.read().decode("utf-8")         
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

@app.route('/contact') 
def contact(): 
    return render_template('contact.html')
