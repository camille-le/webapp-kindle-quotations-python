## Kindle Quotations Project
This project helps people transform their saved quotations from Kindle eBooks into machine-
readable or Excel/Google Sheets-friendly formats (CSV). 

Currently, with the Kindle app, you can email your favorite quotations to yourself, in the
form of an HTML document with CSS formatting. However, the Kindle app does not provide a 
way for a person or computer to easily extract the quotations data. 

This project provides a solution through a web-app, eliminating the need for manual
parsing work. 

Here is a live version of this project: 
https://blastoise.pythonanywhere.com

## Code Style
[Google Python Gide](https://google.github.io/styleguide/pyguide.html)
 
## Screenshots

## Tech/Frameworks Used
<b>Built with</b>
- [Python 3](https://www.python.org/download/releases/3.0/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) 
- [SQL Alchemy](https://www.sqlalchemy.org/)

## Features
* Convert XML files to CSV 


## Installation
Below is an example of how to get a development environment running. 

This is an app written in python3 and Flask. Once you have Python3 installed, add
the following libraries: 

1. Install flask and flask_sqlalchemy 
```bash 
$ pip3 install flask 
$ pip3 install flask_sqlalchemy
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

## Tests
_How to run tests (with code examples)_ 


## How to use this project?


## Contribute

[contributing guideline](https://github.com/zulip/zulip-electron/blob/master/CONTRIBUTING.md)

## Credits
* Repos 
* Blogposts 
* Contributors 

* [MySQL Commands](http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm) 


## License
