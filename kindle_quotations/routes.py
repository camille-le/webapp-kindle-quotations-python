""" 
So how exactly does Flask handle uploads? Well it will store them in the 
webserver’s memory if the files are reasonable small otherwise in a temporary 
location (as returned by tempfile.gettempdir()). But how do you specify 
the maximum file size after which an upload is aborted? By default 
Flask will happily accept file uploads to an unlimited amount of memory, 
but you can limit that by setting the MAX_CONTENT_LENGTH config key:
"""

import os 
import random
from flask import render_template, url_for, flash, redirect, request, send_from_directory 
from werkzeug.utils import secure_filename
from kindle_quotations import app 
from kindle_quotations.models import process


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads'
ALLOWED_EXTENSIONS = {'xml'}

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# limit upload size upto 8mb
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route("/")
@app.route("/home")
def home():    
    return render_template('home.html') 


@app.route("/upload", methods=['GET', 'POST'])
def upload(): 
    
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
            
            # process file information 
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename) 
            process(filepath) 
            
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload.html')    
    

#def process_file(path, filename):
 #   process(path) 
    

 #   remove_watermark(path, filename)    
 # output_stream = open(app.config['DOWNLOAD_FOLDER'] + filename, 'wb')


@app.route('/uploads/<filename>')
def uploaded_file(filename):    
   #return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True) 
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

    