### Kindle Quotations App Project 

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
