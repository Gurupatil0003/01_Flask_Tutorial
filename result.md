
```python
### Integrate HTML With Flask
### HTTP verb GET And POST

##Jinja2 template engine
'''
{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments
'''

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res='FAIL'
    exp={'score':score,'res':res}
    return render_template('result.html',result=exp)


@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=""
    return redirect(url_for('success',score=total_score))

    
if __name__=='__main__':
    app.run(debug=True)
 ```   

# result.py
```python  

<html>

<h2>Final Results</h2>

<body>
<table border=2>
 {% for key,value in result.items() %}
    <tr>
        {# This is the comment sections #}
        <th>{{ key }}</th>
        <th>{{ value }}</th>

    </tr>  
  {% endfor %}
</table>
</body>

</html>


```

# index.html
```python
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="{{ url_for('static',filename='style.css') }}">
<script type="text/javascript" src="{{ url_for('static',filename='script/script.js') }}">
  
</script>

</head>
<body>

<h2>HTML Forms</h2>

<form action="/submit" method='post'>
  <label for="Science">Science:</label><br>
  <input type="text" id="science" name="science" value="0"><br>
  <label for="Maths">Maths:</label><br>
  <input type="text" id="maths" name="maths" value="0"><br><br>
  <label for="C ">C:</label><br>
  <input type="text" id="c" name="c" value="0"><br><br>
  <label for="datascience">Data Science:</label><br>
  <input type="text" id="datascience" name="datascience" value="0"><br><br>
  <input type="submit" value="Submit">
</form> 

<p>If you click the "Submit" button, the form-data will be sent to a page called "/submit".</p>

</body>
</html>

```

# Style.css 
```python
input[type=text], select {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;

} 

input[type=submit], select {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;

} 


```
    
