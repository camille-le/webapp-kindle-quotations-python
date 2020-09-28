import os 
import random
from flask import render_template, url_for, flash, redirect, request 
from werkzeug.utils import secure_filename
from kindle_quotations import app 
from kindle_quotations.models import process


@app.route("/")
@app.route("/home")
def home():

    #book_blob = process().split("\n\n")
    #rand_num = random.randint(3, len(book_blob))

    #book_title = book_blob[0]
    #book_author = book_blob[1]
    #book_citation = book_blob[2]

    #return "<h2>Random Quotations:</h2>" + book_title +"<br>"
    #+ book_author + "<br>" + book_citation + "<br>" + book_blob[rand_num]        
    return render_template('home.html') 

@app.route("/upload", methods=['GET', 'POST'])
def upload():       
    # if request.method == 'POST' 
    return render_template('upload.html')