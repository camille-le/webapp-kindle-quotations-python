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
            flash('No file part')          
            return redirect(request.url)
        file = request.files['file']
        
        # if user does not select file, browser also 
        # submit an empty part without filename 
        if file.filename == '':
            flash('No file selected', category='')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))               
            if request.form['download'] == 'Download CSV':                     
                return download_csv(filename)                                      
    return render_template('home.html') 
    

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

# def download_json(filename):         
#     filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)     
#     data = process(filepath, 'json') # returns a dict 
#     resp = make_response(json.dumps(data)) 
#     response.headers["Content-Disposition"] = "attachment; filename=export.json"
#     resp.headers["Content-type"] = 'application/json'
#     resp.mimetype='application/json'
#     print("some success")
#     return resp

@app.route('/uploads/<filename>')
def uploaded_file(filename):       
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


@app.route('/contact')    
def contact(): 
    form = HTMLtoCSVForm() 
    return render_template('contact.html', title="Testing HTML to CSV", form=form)

