## Kindle Quotations App Project
This project helps people transform their saved quotations from Kindle eBooks into
machine-readable or Excel/Google Sheets-friendly formats (CSV).

Currently, with the Kindle app, you can email your favorite quotations to yourself,
in the form of an HTML document with CSS formatting. However, the Kindle app does not
provide a way for a person or computer to easily extract the quotations data.

<img src="https://github.com/camille-le/webapp-kindle-quotations-python/blob/main/kindle_quotations/static/sample_input.png" alt="Sample web-app"/> 

## Current Features (As of November 4th, 2020) 
* Convert Kindle app's HTML/XML files to CSV and download file 
* Convert Kindle app's HTML/XML files to JSON and download file 
 
## Screenshots

<img src="kindle_quotations/static/sample_kindle_export.png" alt="Sample export from Kindle app" width="300"/>
<img src="kindle_quotations/static/sample_output.png" alt="Sample output file from web-app" width="200" style="float:right"/>

## Tech/Frameworks Used
<b>Built with</b>
- [Python 3.8](https://www.python.org/download/releases/3.0/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

## Installation
Below is an example of how to get a development environment running.

This is an app written in python3 and Flask. Once you have Python3 installed, add the following libraries:

1. Install flask and flask_sqlalchemy
```bash
$ pip3 install flask
$ pip3 install flask_sqlalchemy
$ pip3 install flask_wtf
```
Note, in case you get an error like this:
```
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/Library/Python/3.8'
```
You can add the `--install` flag like so:
```
$ pip3 install flask --user
$ pip3 install flask_sqlalchemy --user
```
2. After installing the libraries, execute the `run.py` file, which will run the app
in debug mode.

3. Open http://127.0.0.1:5000/ or localhost:5000 in your preferred browser

4. Select one of the sample test data from the notebooks folder; select "Choose File"
button and upload. The file will download as a csv relative to your project.


## Credits (Repos, Articles, Blogposts)
_Articles:_
* [MySQL Commands](http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm)
* [Handling File Uploads with Flask](https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask)
* [Flask File Upload Download](https://docs.faculty.ai/user-guide/apis/flask_apis/flask_file_upload_download.html)
* [Flask-WTF Documentation](https://flask-wtf.readthedocs.io/en/latest/form.html#module-flask_wtf.file)
* [io — Core tools for working with streams](https://docs.python.org/3/library/io.html)
