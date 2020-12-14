from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_dropzone import Dropzone
import os 

app = Flask(__name__)
app.secret_key = "[password]" 
dropzone = Dropzone(app)

from kindle_quotations import routes
