import os 
import random
from flask import render_template, url_for, flash, redirect, request, send_from_directory, make_response, jsonify
from werkzeug.utils import secure_filename
from kindle_quotations import app 
from kindle_quotations.models import process
from kindle_quotations.forms import HTMLtoCSVForm
import io; io.StringIO()


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
ALLOWED_EXTENSIONS = {'html', 'xml'}

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 # 1 MB


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home(): 
    form = HTMLtoCSVForm() 
    if form.validate_on_submit():         
        upload_file = form.filename.data # FileStore object         
        fname = secure_filename(upload_file.filename) 
        upload_file.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))
        if form.submit.label.text == "Download CSV":   
            return download_csv(fname)                              
    return render_template('home.html', form=form)


@app.route('/uploads/<filename>')
def uploaded_file(filename):       
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


@app.route('/contact') 
def contact(): 
    return render_template('contact.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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

