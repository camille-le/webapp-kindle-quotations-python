# kindle_quotations

### How do I get Flask Up and Running? 
* Install Flask 
```bash
$ pip3 install flask 
```

### How do I run a Flask app in debug mode? 
Below is a running web server that comes with Flask. 
```bash
# This will point to http://127.0.0.1:5000/ by default
$ python3 -m flask run
```
The alias for "127.0.0.1" is localhost
http://localhost:5000/, which will return the same result. 

### How do I set FLASK_DEBUG to true? 
```bash
export FLASK_DEBUG=1
```
Since we're in debug mode, those changes loaded automatically and we didn't have to restart our web server. 

### How do I use the Flask run command? 
Another option is to set `debug=True`: 

```python3
if __name__ == '__main__':
    app.run(debug=True)
```
Allows us to do this:
`python3 flaskblog.py`

### How do I generate a requirements.txt document? 
```
$ pip3 freeze > requirements.txt
```

### What are `routes`? 
Routes are what we type into our browsers to go to specific pages. In Flask, we use the `@app.route` decorator. Decorators allow you to add existing functionality. In addition, "/" is the root page or home page. 

### How does Flask Handle Uploads? 
It will store them in the webserver’s memory if the files are reasonably small.
 Otherwise, it will store them in a temporary location: 
```python
tempfile.gettempdir() 
```
### How do you specify the maximum file size? 
By default, Flask will accept file uploads to an unlimited amount of memory, 
but you can limit that by setting the MAX_CONTENT_LENGTH config key:
```python
# limit upload size upto 8 MB
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
```

### Misc / TO DO 
* Make sure to set your `env` variable first. 
```
$ export FLASK_APP=flaskblog.py
```

### Sources 
_Information for how to use the Upload/Download tool with Flask:_ 
* https://github.com/viveksb007/camscanner_watermark_remover/blob/master/cam_scanner_remover.py
* https://viveksb007.github.io/2018/04/uploading-processing-downloading-files-in-flask
* https://blog.patricktriest.com/host-webapps-free/
* https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/#an-easier-solution
