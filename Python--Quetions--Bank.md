## 1.How can you add a new key-value pair to a dictionary in Python?
~~~python

my_dict = {'key1': 'geeks', 'key2': 'for'}
print("Current Dict is:", my_dict)

# Adding new key-value pairs
my_dict['key3'] = 'Geeks'
my_dict['key4'] = 'is'
my_dict['key5'] = 'portal'
my_dict['key6'] = 'Computer'

print("Updated Dict is:", my_dict)


~~~

output:-

~~~python

Current Dict is: {'key2': 'for', 'key1': 'geeks'}
Updated Dict is: {'key3': 'Geeks', 'key5': 'portal', 'key6': 'Computer', 'key4': 'is', 'key1': 'geeks', 'key2': 'for'}


~~~


## 2.How do you raise an exception in Python?

Python, you can raise an exception using the raise keyword. This allows you to signal an error condition or handle exceptional situations in your code. Here are a few ways to raise exceptions:

Using the raise Statement: To raise an exception, simply use the raise keyword followed by the type of exception you want to raise. You can also provide an optional error message. For example:

~~~python
Python

try:
    x = -1
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
except Exception as e:
    print(f"An error occurred: {e}")

~~~

## 3.What is the role of the cursor() method in   Python's MySQL database connectivity?

- The cursor() method in Python's MySQL  database connectivity, specifically with  libraries like mysql-connector-python, plays a  vital role in interacting with 
  the database.  Here's a breakdown of its function:

- Creating a Cursor Object:

- When you call cursor() on a MySQL connection   object, it returns a cursor object. This object     acts as an intermediary between your Python  program and the 
  MySQL server.
  Executing Database Operations:

- The cursor object allows you to execute  various database operations, primarily through  the execute() method. You can pass SQL statements (SELECT, INSERT, 
  UPDATE, DELETE, etc.) to execute().
  Fetching Results (for queries):

- If your SQL statement retrieves data (like a  SELECT query), the cursor object helps you  fetch the results one row at a time or in  batches. It provides methods 
  like fetchone(),  fetchall(), etc., to retrieve data.

## 4.What is the Django admin console used for in a Django project?
- One of the most powerful parts of Django is the automatic admin interface. It reads metadata from your models to provide a quick, model-centric interface where 
 trusted users can manage content on your site. The admin’s recommended use is limited to an organization’s internal management tool. It’s not intended for 
 building your entire front end around.

- The Django admin application can use your models to automatically build a site area that you can use to create, view, update, and delete records. This can save 
  you a lot of time during development, making it very easy to test your models and get a feel for whether you have the right data.

#### Creating a superuser

- In order to log into the admin site, we need a user account with Staff status enabled. In order to view and create records we also need this user to have 
  permissions to manage all our objects. You can create a "superuser" account that has full access to the site and all needed permissions using manage.py.

```pythom
python manage.py createsuperuser
```

```python
Username: Guru 
Email address: guru@dummymail.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
My password did not meet the criteria, but this is a test environment, and I choose to create user anyway, by enter y:

Bypass password validation and create user anyway? [y/N]: y
```
- If you press [Enter], you should have successfully created a user:

- Superuser created successfully.

- Now start the server again:

```python
py manage.py runserver
```
In the browser window, type 127.0.0.1:8000/admin/ in the address bar.

<img src="https://github.com/Gurupatil0003/01_Flask_Tutorial/blob/main/Images/Screenshot%202024-03-25%20171440.png"  alt="structure" width="100%"  />

And fill in the form with the correct username and password:

<img src="https://github.com/Gurupatil0003/01_Flask_Tutorial/blob/main/Images/Screenshot%202024-03-25%20171504.png"  alt="structure" width="100%"  />

Now We successfully Login
<img src="https://github.com/Gurupatil0003/01_Flask_Tutorial/blob/main/Images/Screenshot%202024-03-25%20171516.png"  alt="structure" width="100%"  />


### 5.What is the role of HTTP methods in RESTful APIs?


### 6.Describe the purpose of the del keyword in Python.

Python’s del statement is used to delete variables and objects in the Python program. Iterable objects such as user-defined objects, lists, set, tuple, dictionary, variables defined by the user, etc. can be deleted from existence and from the memory locations in Python using the del statement. 


```python
my_list = [1, 2, 3, 4, 5]

# Delete the element at index 2 (value 3)
del my_list[2]

print(my_list)  # Output: [1, 2, 4, 5]
```
## 7.How do you open a file in Python using the open() function?

Python has a built-in **`open()`** function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.

## Syntax
<img src="https://github.com/Gurupatil0003/01_Flask_Tutorial/blob/main/Images/ReadOpen.png"  alt="structure" width="100%"  />

```python

f = open(\"test.txt\")
f = open("test.txt")   # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
```
## 8.What is the role of views in Django and how are they mapped to URLs?

## 9.What is the primary purpose of resource representations in RESTful APIs?

## 10.What do HTTP status codes indicate in RESTful API responses?

- HTTP status codes are three-digit codes that indicate the outcome of an API request. They are included in the API’s response to the API client, and they include 
 important information that helps the client know how to proceed.

- HTTP status codes are essential to the HTTP protocol, which defines how data is transferred between clients and servers on the internet. Anyone who works with 
 web-based technologies should have a solid understanding of these codes, as they provide valuable insight that can be used to troubleshoot issues and improve the 
 user experience.

- Here, we’ll explore the different types of HTTP status codes, highlight the most common ones, and discuss some best practices for implementing them.


## HTTP status codes are grouped into five classes, each beginning with a number that represents the type of response. The classes are:

## Informational - 1xx

This class of status code indicates a provisional response.  There are no 1xx status codes used in REST framework by default.

    HTTP_100_CONTINUE
    HTTP_101_SWITCHING_PROTOCOLS

## Successful - 2xx

This class of status code indicates that the client's request was successfully received, understood, and accepted.

    HTTP_200_OK
    HTTP_201_CREATED
    HTTP_202_ACCEPTED
    HTTP_203_NON_AUTHORITATIVE_INFORMATION
    HTTP_204_NO_CONTENT
    HTTP_205_RESET_CONTENT
    HTTP_206_PARTIAL_CONTENT

## Redirection - 3xx 

This class of status code indicates that further action needs to be taken by the user agent in order to fulfill the request.

    HTTP_300_MULTIPLE_CHOICES
    HTTP_301_MOVED_PERMANENTLY
    HTTP_302_FOUND
    HTTP_303_SEE_OTHER
    HTTP_304_NOT_MODIFIED
    HTTP_305_USE_PROXY
    HTTP_306_RESERVED
    HTTP_307_TEMPORARY_REDIRECT

## Client Error - 4xx

The 4xx class of status code is intended for cases in which the client seems to have erred.  Except when responding to a HEAD request, the server SHOULD include an entity containing an explanation of the error situation, and whether it is a temporary or permanent condition.

    HTTP_400_BAD_REQUEST
    HTTP_401_UNAUTHORIZED
    HTTP_402_PAYMENT_REQUIRED
    HTTP_403_FORBIDDEN
    HTTP_404_NOT_FOUND
    HTTP_405_METHOD_NOT_ALLOWED
    HTTP_406_NOT_ACCEPTABLE
    HTTP_407_PROXY_AUTHENTICATION_REQUIRED
    HTTP_408_REQUEST_TIMEOUT
    HTTP_409_CONFLICT
    HTTP_410_GONE
    HTTP_411_LENGTH_REQUIRED
    HTTP_412_PRECONDITION_FAILED
    HTTP_413_REQUEST_ENTITY_TOO_LARGE
    HTTP_414_REQUEST_URI_TOO_LONG
    HTTP_415_UNSUPPORTED_MEDIA_TYPE
    HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
    HTTP_417_EXPECTATION_FAILED
    HTTP_428_PRECONDITION_REQUIRED
    HTTP_429_TOO_MANY_REQUESTS
    HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE

## Server Error - 5xx

Response status codes beginning with the digit "5" indicate cases in which the server is aware that it has erred or is incapable of performing the request.  Except when responding to a HEAD request, the server SHOULD include an entity containing an explanation of the error situation, and whether it is a temporary or permanent condition.

    HTTP_500_INTERNAL_SERVER_ERROR
    HTTP_501_NOT_IMPLEMENTED
    HTTP_502_BAD_GATEWAY
    HTTP_503_SERVICE_UNAVAILABLE
    HTTP_504_GATEWAY_TIMEOUT
    HTTP_505_HTTP_VERSION_NOT_SUPPORTED
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED



## 11.How can you check if a value exists in a set in Python?
```python
my_set = {1, 2, 3, 4, 5}

# Check if a value exists in the set
if 3 in my_set:
    print("3 exists in the set")
else:
    print("3 does not exist in the set")

# Check if a value does not exist in the set
if 6 not in my_set:
    print("6 does not exist in the set")
else:
    print("6 exists in the set")
```
### output
```python

3 exists in the set
6 does not exist in the set


```
## 12.What is the purpose of abstraction in object-oriented programming?

## 13.What is the purpose of Python libraries like pymysql and pymongo?
| Feature                | pymysql                                                  | pymongo                                                |
|------------------------|----------------------------------------------------------|--------------------------------------------------------|
| Purpose                | Python client library for MySQL databases                | Python driver for MongoDB databases                    |
|                        |                                                          |                                                        |
| **Connection**         | Establish connections to MySQL databases                 | Establish connections to MongoDB databases             |
| **Query Execution**    | Execute SQL queries and statements                      | Insert, query, update, and delete documents           |
| **Result Handling**    | Fetch query results as Python objects                   | N/A (Documents returned as dictionaries)              |
| **Transactions**       | Handle transactions                                     | N/A (MongoDB uses atomic operations on single documents)|
|                        |                                                          |                                                        |
| **Typical Use Cases**  | Building web applications with MySQL backends           | Developing web applications with MongoDB backends     |
|                        | Data analysis and manipulation with MySQL databases     | Building scalable and flexible data storage solutions with MongoDB |
|                        | Integrating MySQL databases into Python-based projects | Analyzing large datasets stored in MongoDB collections |
|                        |                                                          | Integrating MongoDB databases into Python-based applications (IoT projects, analytics platforms, etc.) |


## 14.How do URLs contribute to RESTful API design?
REST (Representational State Transfer) API URLs (Uniform Resource Locators) are specific addresses used to access and interact with resources within a specific RESTful API. These addresses are unique, each one leading to a specific data or functionality within the REST API.

### REST API URLs Strucutre
- To be able to reproduce REST API URLs in a standardized manner, REST API URLs have a common shared structure, which consists of:

- Protocol: Protocols are usually in the form of HTTP or HTTPS, which specify how to communicate with the API.
- Host: The host defines the server address where the API resides (e.g., api.example.com).
- Path: A path defines the specific resource within the API, starting with a forward slash (e.g., /users).
- Query String (optional): Query strings, which are optional, allow developers to add additional parameters that can filter or refine the resource, using key- 
  value pairs after a question mark (e.g., /users?name=John).


### Why Do We Need to Understand REST API URLs?
- There are a variety of reasons why web developers are required to understand the core concept of REST API URLs. These are a few of the main reasons:

- Clarity and Precision: By understanding a REST API URL, you can identify specific resources, ensuring accurate interactions.
  Usability and Consistency: Well-structured REST API URLs promote ease of understanding and prediction.
  Interoperability and Standards: Following best practices for REST API URLs enables smooth communication with various tools and applications, making it easier 
  for other developers to use your API
  Versioning and Evolution: Clear versioning schemes aid in managing REST API URL updates and maintaining compatibility.
  Security and Control: REST API URLs can be designed to limit access to sensitive data from the public or malicious users.

### Examples of REST API URLs
- If you are wondering what REST API URLs look like, here are a few real-world samples of REST API URLs that you may have come across before reading this article!

- GitHub: https://api.github.com/users/Bard retrieves information about the user "Bard".
- OpenWeatherMap: https://api.openweathermap.org/data/2.5/weather?q=London gets weather data for London.
- Unsplash: https://api.unsplash.com/photos/random?count=1 retrieves one random photo.
- These REST API URLs are commonly seen as the website address, which changes whenever a relay of data is required, or when you change web pages.

## 15.What function is used to convert a string to lowercase in Python?
In Python, you can use the lower() method to convert a string to lowercase. This method returns a copy of the string with all uppercase characters converted to lowercase.

Here's how you can use the lower() method:
```python
my_string = "Hello World"
lowercase_string = my_string.lower()
print(lowercase_string)  # Output: hello world

```
## 16.How is the super() function utilized in Python?

- he super() function in Python is used to access methods and properties from a parent or superclass within a subclass. It provides a way to delegate method calls 
  to the parent class, allowing you to invoke methods defined in the superclass without explicitly naming the superclass.

- When a class inherits all properties and behavior from the parent class is called inheritance. In such a case, the inherited class is a subclass and the latter 
  class is the parent class.

- In child class, we can refer to parent class by using the super() function. Python super() function returns a temporary object of the parent class that allows 
 us to call a parent class method inside a child class method.

- Benefits of using the super() function are:

- We are not required to remember or specify the parent class name to access its methods.
- We can use the super() function in both single and multiple inheritances.
- The super() function support code reusability as there is no need to write the entire function
  
```python

# Example 1:

class Company:
    def company_name(self):
        return 'Google'

class Employee(Company):
    def info(self):
        # Calling the superclass method using super()function
        c_name = super().company_name()
        print("Arthur works at", c_name)

# Creating object of child class
emp = Employee()
emp.info()

```

- note:
 In the above example, we create a parent class Company and child class Employee. In Employee class, we call the parent class method by using a super() function.

## 17.What data structures in Python are similar to lists but are immutable?

- In Python, the data structure that is similar to a list but immutable is called a tuple.
- 
- Tuples are almost identical to lists, so they contain an ordered collection of elements, except for one property: they are immutable. We would use tuples if we 
 needed a data structure that, once created, cannot be modified anymore.

- A tuple is an ordered collection of elements, similar to a list, but it is immutable, meaning its elements cannot be changed or modified after creation. Tuples 
 are defined using parentheses () and can contain elements of any data type, including other tuples.
## 18.What is the term for the process of bundling data and methods together within a class?


## 19.Which method is used to insert a document into a MongoDB collection using PyMongo?

```pytohn
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
mycollection = db["mycollection"]

# Insert a single document
data = {"name": "John", "age": 30}
result = mycollection.insert_one(data)

```
## 20.For what purpose does the Django admin console provide a user interface?
- The Django admin console provides a user interface for the purpose of managing the data and functionality of a Django web application. It serves as an - 
  administrative interface for interacting with the backend of the application without writing custom views or forms. Some of the key purposes of the Django admin 

### console are:

- Data Management: Admins can manage (create, read, update, delete) the data stored in the application's database. This includes CRUD operations on models defined 
 in the Django application.

- User Authentication and Authorization: Admins can manage user accounts, permissions, and groups. They can create, modify, and delete user accounts, assign 
 specific permissions to users, and group users based on their roles.

- Customization: The Django admin console is highly customizable. Developers can customize the appearance and behavior of the admin interface by modifying the 
 admin site configuration, adding custom admin views, and overriding admin templates.

- Logging and Monitoring: Admins can view and analyze logs, perform monitoring tasks, and track user activity within the admin interface. They can monitor changes 
 made to data by users and track system events.

- Debugging and Troubleshooting: The admin console can be used for debugging and troubleshooting purposes. Admins can view detailed error messages, inspect 
 database queries, and diagnose issues with data integrity or application functionality.

- Overall, the Django admin console provides a convenient and powerful interface for administrators to manage various aspects of a Django application, thereby 
  streamlining the process of backend administration and reducing the need for manual intervention.

 ## 21.Which Python library is commonly used for consuming RESTful APIs? 

- The Python library commonly used for consuming RESTful APIs is called requests.

- The requests library is a popular HTTP library for making HTTP requests in Python. It provides a simple and intuitive API for interacting with RESTful APIs, 
 allowing you to send HTTP requests, handle responses, and work with JSON data easily.

- Here's a basic example of how to use the requests library to make a GET request to a RESTful API:

```python
import requests

# Make a GET request to a RESTful API endpoint
response = requests.get('https://api.example.com/data')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)
```

 ## 22.Which keyword is used to exit a loop prematurely in Python?
- he keyword used to exit a loop prematurely in Python is break.

- The break keyword is used within loops (such as for and while loops) to terminate the loop prematurely when a certain condition is met. When break is 
 encountered within a loop, the loop is immediately exited, and the program continues with the next statement after the loop.

- Here's an example of using break to exit a loop:

```python
# Example using a while loop
i = 0
while i < 5:
    print(i)
    if i == 3:
        break  # Exit the loop when i equals 3
    i += 1

# Example using a for loop
for i in range(5):
    print(i)
    if i == 3:
        break  # Exit the loop when i equals 3
```

## 23.In MySQL database connectivity with Python, which method is used to execute SQL queries?
```python
import pymysql

# Connect to MySQL
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='mgpatils',
                             database='patils',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # Create a cursor object
    with connection.cursor() as cursor:
        # SQL query to execute
        sql_query = "SELECT * FROM routess"

        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch the result
        result = cursor.fetchall()

        # Process the result
        for row in result:
            print(row)

finally:
    # Close the connection
    connection.close()
```

## 24.What administrative tasks can be performed using the Django admin console?

- The Django admin console provides a user-friendly interface for performing various administrative tasks in a Django web application. Some of the key 
 administrative tasks that can be performed using the Django admin console include:

- Managing Models: Admins can manage the data stored in the application's database by performing CRUD (Create, Read, Update, Delete) operations on the models 
 defined in the Django application. This includes adding, editing, and deleting records from the database tables.

- User Authentication and Authorization: Admins can manage user accounts, permissions, and groups. They can create, modify, and delete user accounts, assign 
 specific permissions to users, and group users based on their roles. The Django admin console provides built-in support for user authentication and authorization.

- Customization: The Django admin console is highly customizable. Developers can customize the appearance and behavior of the admin interface by modifying the 
 admin site configuration, adding custom admin views, and overriding admin templates. This allows developers to tailor the admin interface to suit the specific 
 requirements of the application.

- Logging and Monitoring: Admins can view and analyze logs, perform monitoring tasks, and track user activity within the admin interface. They can monitor changes 
 made to data by users, track system events, and analyze usage patterns. The Django admin console provides tools for logging and monitoring activities within the 
 application.

- Debugging and Troubleshooting: The Django admin console can be used for debugging and troubleshooting purposes. Admins can view detailed error messages, inspect 
 database queries, and diagnose issues with data integrity or application functionality. They can also view system logs and analyze error reports to identify and 
 fix problems.

- Overall, the Django admin console serves as a powerful tool for managing and administering Django web applications, providing a convenient and centralized 
 interface for performing a wide range of administrative tasks.

## 25.Difference Between Set and Dictionary in Python: Set vs Dictionary

| Parameter    | Set                                          | Dictionary                                      |
|--------------|----------------------------------------------|-------------------------------------------------|
| Definition   | An unordered collection of unique elements. | An ordered collection of key-value pairs.       |
| Representation | Curly braces {}.                             | Curly braces {}, but with key-value pairs.     |
| Order        | Unordered.                                    | Ordered (from Python 3.7 onwards).              |
| Duplicates   | Does not allow duplicate elements.            | Does not allow duplicate keys.                  |
| Mutability   | Mutable (can add or remove elements).        | Mutable (can add, modify, or remove key-value pairs). |
| Access Method| Elements are accessed directly.               | Values are accessed using keys.                 |
| Use Case     | To store unique elements.                     | To store related pieces of information.         |
| Example      | `my_set = {1, 2, 3}`                         | `my_dict = {"name": "Alice", "age": 30}`       |

## 26.How do you handle a ZeroDivisionError exception in Python?

- In Python, you can handle a ZeroDivisionError exception using a try-except block. Here's how you can handle the ZeroDivisionError:
```python
try:
    result = numerator / denominator
except ZeroDivisionError:
    # Handle the ZeroDivisionError exception
    print("Error: Division by zero is not allowed.")

```
In this code:

- The code inside the try block attempts to perform a division operation.
- If the division operation encounters a division by zero, a ZeroDivisionError exception is raised.
- The except ZeroDivisionError block catches the ZeroDivisionError exception.
- Inside the except block, you can specify the actions to take when a ZeroDivisionError occurs. In this example, it simply prints an error message, but you can - - customize the handling based on your requirements.
- By using a try-except block to handle the ZeroDivisionError, you can gracefully handle the error and prevent your program from crashing.

## 27


## 28.What is Routing in Flask?
- App Routing means mapping the URLs to a specific function that will handle the logic for that URL. Modern web frameworks use more meaningful URLs to help users   remember the URLs and make navigation simpler. 

- Example: In our application, the URL (“/”) is associated with the root URL. So if our site’s domain was www.example.org and we want to add routing to 
 “www.example.org/hello”, we would use “/hello”. 

- To bind a function to an URL path we use the app.route decorator. In the below example, we have implemented the above routing in the flask.

```python
from flask import Flask 

app = Flask(__name__) 

# Pass the required route to the decorator. 
@app.route("/hello") 
def hello(): 
	return "Hello, Welcome to GeeksForGeeks"
	
@app.route("/") 
def index(): 
	return "Homepage of GeeksForGeeks"

if __name__ == "__main__": 
	app.run(debug=True) 
```
- The hello function is now mapped with the “/hello” path and we get the output of the function rendered on the browser.

Step to run the application: Run the application using the following command.
```python
python main.py
```
![image](https://github.com/Gurupatil0003/01_Flask_Tutorial/assets/110026505/452a0c98-24f1-4aab-b513-9035f1434f64)
<img src="(https://github.com/Gurupatil0003/01_Flask_Tutorial/assets/110026505/452a0c98-24f1-4aab-b513-9035f1434f64"  alt="structure" width="100%"  />

## 44.Write a program to demonstrate how to insert a row into the table using MySQL and Python.
~~~python
import pymysql

def insert_row(data):
    try:
        # Establish a connection to the MySQL database
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='mgpatils',
                                     database='Guru')

        # Create a cursor object
        cursor = connection.cursor()

        # SQL INSERT statement with placeholders
        sql = "INSERT INTO people (name, age) VALUES (%s, %s)"

        # Execute the SQL INSERT statement with the provided data
        cursor.execute(sql, data)
        
        # Commit the transaction
        connection.commit()
        print("Row inserted successfully!")
        
    except Exception as e:
        # Rollback the transaction in case of an error
        connection.rollback()
        print("Error:", e)
        
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

# Example data to insert into the table
data_to_insert = ('John', 30)

# Call the insert_row function with the example data
insert_row(data_to_insert)


~~~
## Select query using MySQL and Python


- To execute a SELECT query using MySQL and Python with the pymysql library, follow these steps:

- Import the pymysql module: First, import the pymysql module in your Python script.

- Establish a connection to the MySQL database: Use the pymysql.connect() function to establish a connection to your MySQL database. Provide the necessary connection parameters such as host, user, password, and database name.

- Create a cursor object: Once the connection is established, create a cursor object using the cursor() method of the connection object. The cursor object will be used to execute SQL queries.

- Execute SQL SELECT statement: Use the execute() method of the cursor object to execute an SQL SELECT statement.   Provide the SELECT statement as a string.

- Fetch data from the cursor: After executing the SELECT statement, use the fetchall() or fetchone() method of the     cursor object to fetch the result set. This method returns the query results as a tuple or a list of tuples.

- Process the query results: Process the fetched data as needed in your Python script.

- Close the cursor and connection: Finally, close the cursor and connection using the close() method of the cursor and    connection objects, respectively.
~~~python
import pymysql

def execute_select_query():
    try:
        # Establish a connection to the MySQL database
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='mgpatils',
                                     database='Guru')

        # Create a cursor object
        cursor = connection.cursor()

        # SQL SELECT statement
        sql = "SELECT * FROM people"

        # Execute the SQL SELECT statement
        cursor.execute(sql)

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Process the query results
        for row in rows:
            print(row)

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

# Call the execute_select_query function to execute the SELECT query
execute_select_query()
~~~

## 48.Delete query using MySQL and Python
- To execute a DELETE query using MySQL and Python with the pymysql library, you can follow these steps:

- Import the pymysql module: First, import the pymysql module in your Python script.

- Establish a connection to the MySQL database: Use the pymysql.connect() function to establish a connection to your  MySQL database. Provide the necessary connection parameters such as host, user, password, and database name.

- Create a cursor object: Once the connection is established, create a cursor object using the cursor() method of the connection object. The cursor object will be used to execute SQL queries.

- Execute SQL DELETE statement: Use the execute() method of the cursor object to execute an SQL DELETE statement. Provide the DELETE statement as a string.

- Commit the transaction: After executing the DELETE statement, commit the transaction using the commit() method of the connection object to save the changes to the database.

- Close the cursor and connection: Finally, close the cursor and connection using the close() method of the cursor and connection objects, respectively.

- Here's an example demonstrating how to execute a DELETE query using pymysql:

~~~python

import pymysql

def execute_delete_query():
    try:
        # Establish a connection to the MySQL database
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='mgpatils',
                                     database='Guru')

        # Create a cursor object
        cursor = connection.cursor()

        # SQL DELETE statement
        sql = "DELETE FROM people WHERE condition"

        # Execute the SQL DELETE statement
        cursor.execute(sql)

        # Commit the transaction
        connection.commit()
        print("Rows deleted successfully!")

    except Exception as e:
        # Rollback the transaction in case of an error
        connection.rollback()
        print("Error:", e)

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

# Call the execute_delete_query function to execute the DELETE query
execute_delete_query()



~~~~

