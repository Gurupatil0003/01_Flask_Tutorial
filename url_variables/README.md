
```python
  
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# string
@app.route('/string/<string:value>')
def string(value):
    return f"<p>Hi this is a string value {value}</p>"

# int
@app.route('/int/<int:value>')
def int(value):
    return f"<p>Hi this is a int value {value}</p>"

# float
@app.route('/float/<float:value>')
def float(value):
    return f"<p>Hi this is a float value {value}</p>"

# path
@app.route('/path/<path:value>')
def path(value):
    return f"<p>Hi this is a path value {value}</p>"

# uuid
@app.route('/uuid/<uuid:value>')
def uuid(value):
    return f"<p>Hi this is a uuid value {value}</p>"



if __name__=="__main__":
    app.run(debug=True)
    
```
