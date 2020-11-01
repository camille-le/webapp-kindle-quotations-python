import os 
import random
from flask import render_template, url_for, flash, redirect, request, send_from_directory, make_response
from werkzeug.utils import secure_filename
from kindle_quotations import app 
from kindle_quotations.models import process


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads'
ALLOWED_EXTENSIONS = {'xml'}

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# Max File Size is 1 MB
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
@app.route("/home", methods=['GET','POST'])
def home():            
    if request.method == 'POST':        
        # check if the post request has the file part 
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also 
        # submit an empty part without filename 
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))           
            return download(filename)            
    return render_template('home.html') 
    

def download(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename) 
    csv = process(filepath)     
    response = make_response(csv)    
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    response.headers["Content-type"] = "text/csv"
    response.mimetype='text/csv'
    return response


@app.route('/uploads/<filename>')
def uploaded_file(filename):       
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


@app.route('/contact')    
def contact(): 
    return render_template('contact.html')