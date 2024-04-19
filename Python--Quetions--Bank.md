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
- Encapsulation is an important concept in object-oriented programming that allows you to bundle data and methods together within a class, hiding the internal 
 details and providing controlled access to the data. Python supports encapsulation through various mechanisms, enabling you to achieve data hiding and maintain 
 the integrity of your objects. In this article, we will explore encapsulation in Python and how it helps achieve data hiding. Whether you are a beginner or an 
 experienced programmer in domains like machine learning, data science, or artificial intelligence, understanding encapsulation is crucial for writing secure and 
 maintainable Python code.

<img src="https://github.com/Gurupatil0003/01_Flask_Tutorial/assets/110026505/baa3b2f3-92a7-4987-b8a1-8135834893e3"  alt="structure" width="100%"  />

#### Encapsulation and Data Hiding
- Encapsulation is one of the core principles of object-oriented programming, along with inheritance and polymorphism. It involves bundling data (attributes) and 
 methods together within a class and controlling access to the data from outside the class. By encapsulating data, you protect it from unauthorized access and 
 manipulation, ensuring the integrity of the object’s internal state.

- Python provides mechanisms to achieve data hiding, indicating that the internal details of an object should not be directly accessible from outside the class. 
 This is typically done by using access modifiers such as public, protected, and private.

- Public attributes/methods: Public attributes and methods are accessible from anywhere, both inside and outside the class. In Python, by default, all attributes 
 and methods are considered public.

- Protected attributes/methods: Protected attributes and methods are indicated by a single underscore (_) prefix. They are intended to be used within the class 
 and its subclasses. Although they can be accessed from outside the class, it is generally considered a convention not to do so.

- Private attributes/methods: Private attributes and methods are indicated by a double underscore (__) prefix. They are intended to be used only within the class 
 and are not accessible from outside the class. Python internally performs name mangling to make the attribute/method name unique within the class, but they can 
 still be accessed using a specific naming convention.

<img src="https://github.com/Gurupatil0003/01_Flask_Tutorial/assets/110026505/5edfac47-1ddb-453b-9c80-e171ead806eb"  alt="structure" width="100%"  />

- Example: Encapsulation and Data Hiding in Python
- Consider a class Person that represents a person’s information, including their name and age. We’ll demonstrate the use of access modifiers to achieve data 
 hiding.
```python
class Person:
    def __init__(self, name, age):
        self._name = name  # protected attribute
        self.__age = age   # private attribute

    def display(self):
        print(f"Name: {self._name}, Age: {self.__age}")

    def _method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")

    def access_private_method(self):
        self.__private_method()  # accessing private method
```
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
- It opens the browser
<img src="(https://github.com/Gurupatil0003/01_Flask_Tutorial/assets/110026505/452a0c98-24f1-4aab-b513-9035f1434f64"  alt="structure" width="100%"  />

## 29.What is the primary purpose of resource representations in RESTful APIs?

- State means data Representational means formats (such as XML, JSON, YAML, HTML, etc) Transfer means carry data between consumer and provider using the HTTP protocol

- What is REST API?
- To understand what is a REST API, let’s, first of all, understand what is an API. An API stands for an application programming interface. It defines how 
 applications or devices can connect to and communicate with each other.

- A REST (Representational State Transfer) API is an architectural style for an API that uses HTTP (Hypertext Transfer Protocol) request methods to access and 
 manipulate data over the Internet. The most popular HTTP request methods (which are explained below) are GET, POST, PUT, DELETE, PATCH, HEAD, TRACE, CONNECT and 
 OPTIONS.

- One of the examples of when REST APIs are used is when we need to expose back-end systems and data to front-end developers in a standardized format. That's why 
 REST APIs architecture is vital when it comes to building web services that are consumed by a wide range of clients such as browsers, desktop applications and 
 mobile devices.

### HTTP Methods
- HTTP (Hypertext Transfer Protocol) is a protocol that allows communication between clients and servers on the World Wide Web. There exist several dozen 
 different HTTP Methods that can be used for different purposes. The main 9 most popular HTTP Methods are explained below.

- GET - Retrieves data from the server.
- POST - Submits data to be processed to the server.
- PUT - Updates data on the server.
- DELETE - Deletes data from the server.
- PATCH - Applies partial modifications to a resource.
- HEAD - Retrieves only the headers of a resource without the body.
- OPTIONS - Retrieves the HTTP methods supported by a server for a specified URL.
- TRACE - Echoes back the received request to the client, useful for testing or debugging.
- CONNECT - Converts the request connection to a transparent TCP/IP tunnel, usually used for HTTPS tunneling through proxy servers.


## 30.What is the purpose of the in keyword in Python? Provide an example.
- In Python, the in keyword is used to check for membership in a sequence, such as a list, tuple, string, or dictionary keys. It returns True if the specified 
  value is found in the sequence, otherwise False.
  
```python
# Using 'in' with lists
fruits = ['apple', 'banana', 'orange']
print('banana' in fruits)  # Output: True
print('grape' in fruits)   # Output: False

# Using 'in' with strings
sentence = 'The quick brown fox jumps over the lazy dog'
print('brown' in sentence)   # Output: True
print('cat' in sentence)      # Output: False

# Using 'in' with dictionaries (checks for keys)
person = {'name': 'John', 'age': 30, 'city': 'New York'}
print('age' in person)   # Output: True
print('gender' in person)   # Output: False
```
## 31.Describe how you would handle a FileNotFoundError in Python.
- In each case, the in keyword checks whether the specified value is present in the given sequence or dictionary keys.

- Handling a FileNotFoundError in Python involves anticipating the possibility of the file not being found and implementing appropriate error handling to 
 gracefully deal with this situation. Here's how you can handle a FileNotFoundError:

- Use a Try-Except Block: Enclose the code that may raise a FileNotFoundError within a try-except block. This allows you to catch the exception and handle it 
 appropriately.
```python
try:
    # Attempt to open the file
    with open('myfile.txt', 'r') as file:
        # Read or perform operations on the file
        pass
except FileNotFoundError:
    # Handle the FileNotFoundError
    print("File not found or cannot be opened.")

```
## 33.Explain the role of HTTP methods GET, POST, PUT, and DELETE in RESTful APIs.

#### HTTP Methods
- HTTP (Hypertext Transfer Protocol) is a protocol that allows communication between clients and servers on the World Wide Web. There exist several dozen 
 different HTTP Methods that can be used for different purposes. The main 9 most popular HTTP Methods are explained below.

- GET: The GET method is used to retrieve data from the server. It requests a representation of the specified resource and does not modify the resource's state on 
 the server. It's typically used for safe and idempotent operations, meaning it should not change the state of the server and can be repeated multiple times with 
 the same result.

- POST: The POST method is used to submit data to the server to create a new resource. It requests that the server accept the data enclosed in the request payload 
 and store it under the specified URI. It's commonly used for creating new resources, submitting form data, or uploading files.

- PUT: The PUT method is used to update an existing resource or create a new resource if it doesn't exist at the specified URI. It replaces the entire resource 
 with the request payload. It's idempotent, meaning that multiple identical requests should have the same effect as a single request.

- DELETE: The DELETE method is used to request the removal of a resource identified by the specified URI. It's used to delete the resource from the server. Like 
 PUT, it's also idempotent, meaning that making multiple identical requests has the same effect as a single request.

#### Here's a summary of their roles:

- GET: Retrieve data.
- POST: Create a new resource.
- PUT: Update or create a resource.
- DELETE: Remove a resource.

- These HTTP methods, when used in accordance with RESTful principles, enable the creation of APIs that are intuitive, efficient, and scalable. They map CRUD 
 (Create, Read, Update, Delete) operations to standard HTTP methods, making it easier for developers to understand and interact with the API resources.

## 34.How do you establish a connection to a MySQL database in Python using the pymysql library?

To establish a connection to a MySQL database in Python using the pymysql library, you need to follow these steps:

Install the pymysql library if you haven't already. You can install it using pip:
```python
pip install pymysql
```
- Import the pymysql module in your Python script.
- Use the connect() function from pymysql to establish a connection to the MySQL database server by providing the necessary connection parameters such as host, 
 user, password, and database name.
- Optionally, you can handle exceptions such as pymysql.err.OperationalError and pymysql.err.MySQLError to manage connection errors gracefully.

- Here's a basic example:

```python
import pymysql

# Connection parameters
host = 'localhost'
user = 'root'
password = 'mgpatilss'
database = 'Guru'

try:
    # Establish connection
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=database,
                                 cursorclass=pymysql.cursors.DictCursor)

    # Create a cursor object
    cursor = connection.cursor()

    # Execute SQL queries
    cursor.execute("SELECT * FROM your_table")

    # Fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except pymysql.err.OperationalError as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
```



This code establishes a connection to the MySQL database, executes a SELECT query, fetches the results, and prints them. It also handles connection errors gracefully using exception handling.

## 35.Explain the difference between a shallow copy and a deep copy of a list in Python.

In Python, when you want to create a copy of a list, you can use either a shallow copy or a deep copy. Here's the difference between the two:

#### Shallow Copy:
- A shallow copy creates a new list object, but it does not create new objects for the elements within the list. Instead, it copies the references to the objects.
 If the original list contains mutable objects (e.g., lists, dictionaries), changes made to these mutable objects in the copied list will also affect the original 
 list and vice versa.
- Shallow copy can be performed using slicing [:] or the copy() method from the copy module.
```python
original_list = [1, [2, 3], 4]
shallow_copied_list = original_list[:]
# Or: shallow_copied_list = original_list.copy()

original_list[1][0] = 'a'
print(original_list)  # Output: [1, ['a', 3], 4]
print(shallow_copied_list)  # Output: [1, ['a', 3], 4]
```
#### Deep Copy:
A deep copy creates a new list object and recursively creates new objects for all the elements within the list, including nested objects.
Changes made to the elements in the copied list will not affect the original list, and vice versa.
Deep copy can be performed using the deepcopy() function from the copy module.
```python
import copy

original_list = [1, [2, 3], 4]
deep_copied_list = copy.deepcopy(original_list)

original_list[1][0] = 'a'
print(original_list)  # Output: [1, ['a', 3], 4]
print(deep_copied_list)  # Output: [1, [2, 3], 4]
```
In summary, while a shallow copy creates a new list object but shares the references to nested objects with the original list, a deep copy creates a completely new list with new copies of all nested objects, ensuring independence between the original and copied lists.

## 36.How do you implement method overriding in Python?
- Method overriding in Python allows a subclass to provide a specific implementation of a method that is already defined in its superclass. This allows the 
 subclass to customize the behavior of the method without modifying the superclass implementation. Method overriding is achieved by defining a method in the 
 subclass with the same name and signature as a method in the superclass. Here's how you implement method overriding in Python:

- Define a superclass with a method that you want to override:
```python
class Animal:
    def make_sound(self):
        print("Generic animal sound")
```
- Create a subclass that inherits from the superclass and define a method with the same name and signature:
```python
class Dog(Animal):
    def make_sound(self):
        print("Bark")
```
Now, when you create an instance of the subclass and call the overridden method, the subclass method will be executed instead of the superclass method:
```python
animal = Animal()
animal.make_sound()  # Output: Generic animal sound

dog = Dog()
dog.make_sound()  # Output: Bark
```
In this example, the make_sound() method is overridden in the Dog subclass. When you call make_sound() on a Dog instance, it prints "Bark" instead of "Generic animal sound" because the subclass method overrides the superclass method.


## 37.How do you define and register models in a Django project?
- Creating and Registering Models
#### Follow these steps to create and register models in Django:

#### Step 1: Define Your Model
- Open your Django app’s models.py file. This is where you define your models.

- Define a model class by creating a Python class that inherits from django.db.models.Model. For example, let’s create a simple Product model:

```python
# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

```
- In this example, we’ve created a Product model with fields for name, description price and is_published.

#### Step 2: Migrate Your Model
- Django uses migrations to create and update database tables based on your model definitions.

- Create an initial migration for your app:
```python
 python manage.py makemigrations your_app_name
```
 Replace your_app_name with the name of your Django app.

- Apply the migrations to create the database table:

```python
 python manage.py migrate
```
#### Step 3: Register Your Model with the Admin Panel
- Django’s admin panel provides a convenient interface for managing your database records. To make your model accessible via the admin panel:
- Create an admin file for your app if it doesn’t already exist. In your app’s directory, create a file named admin.py.
- Register your model in the admin.py file:
```python
# admin.py
from django.contrib import admin
from .models import Product

admin.site.register(Product)
```
- This code imports the Product model and registers it with the admin panel.

#### Step 4: Customize the Admin Panel (Optional)
- You can further customize how your model is displayed in the admin panel by creating an admin class for it. For instance, you can specify which fields to 
 display, search by, and filter on in the admin list view.

```python
# admin.py
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
Learn more about How to Customize Django Admin Interface
```
#### Step 5: Create Superuser
- Before accessing the admin panel, create a superuser account with administrative privileges:
```python
python manage.py createsuperuser
```
Follow the prompts to set up your superuser account.

##### Step 6: Run the Development Server
- Start your Django development server:
```python
python manage.py runserver
```
- Access the admin panel in your web browser at http://127.0.0.1:8000/admin/, and log in using the superuser credenttials.

#### Step 7: Add Data via the Admin Panel

- In the admin panel, you can now add, view, edit, and delete Product records. Click “Products” under your app’s section to manage the data.

## 38.What are the basic CRUD operations, and how are they performed in PyMongo for MongoDB?
- CRUD operations stand for Create, Read, Update, and Delete, which are fundamental operations used to manipulate data in a database.

- In PyMongo, the Python driver for MongoDB, you can perform CRUD operations as follows:

#### Create (Insert):
- To insert documents into a MongoDB collection, you can use the insert_one() or insert_many() methods.Example (Inserting a Single Document):
```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Access database and collection
db = client['your_database']
collection = db['your_collection']

# Insert a single document
document = {"name": "John", "age": 30}
result = collection.insert_one(document)
```
#### Read (Retrieve):
- To retrieve documents from a MongoDB collection, you can use methods like find_one() or find().Example (Finding a Single Document):
```python
# Find a single document
document = collection.find_one({"name": "John"})
```
- Example (Finding Multiple Documents):
```python
# Find multiple documents
cursor = collection.find({"age": {"$gte": 25}})
for document in cursor:
    print(document)
```
#### Update:
To update documents in a MongoDB collection, you can use methods like update_one() or update_many().Example (Updating a Single Document):
```python
# Update a single document
collection.update_one({"name": "John"}, {"$set": {"age": 35}})

```
#### Delete:
- To delete documents from a MongoDB collection, you can use methods like delete_one() or delete_many().Example (Deleting a Single Document):
```python
# Delete a single document
collection.delete_one({"name": "John"})
```
- Example (Deleting Multiple Documents):
```python
# Delete multiple documents
collection.delete_many({"age": {"$gte": 30}})
```
These are the basic CRUD operations performed in PyMongo for MongoDB. Each operation allows you to interact with MongoDB collections to manage data effectively.

## 39.Describe how you would handle a FileNotFoundError in Python.
- Handling a FileNotFoundError in Python involves using exception handling to gracefully manage situations where a file cannot be found. Here's how you can 
 handle it:

```python
try:
    # Attempt to open the file
    with open('file.txt', 'r') as file:
        data = file.read()
    # Process the file data
    print("File contents:", data)

except FileNotFoundError:
    # Handle the case where the file is not found
    print("File not found.")

```
#### In this example:

- The try block attempts to open the file named 'file.txt' in read mode and reads its contents.
- If the file is found and successfully opened, the data is processed.
- If a FileNotFoundError occurs (i.e., the file does not exist), the control flow moves to the except block, where you can specify how to handle this situation.
- In this case, the program prints "File not found."
- By using try and except, you can ensure that your program doesn't crash when encountering a FileNotFoundError, allowing you to handle the error gracefully and 
 provide appropriate feedback to the user or take alternative actions as needed.

## 40.Discuss the role of templates in Django and how they are rendered.

## 41.A program that generates a random password of a specified length.
```python
import random
import string
def generate_password(length=8):
    # Define the characters to use in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use the random module to generate the password
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password

password_length_str = input("Input the desired length of your password:")
if password_length_str:
    password_length = int(password_length_str)
else:
    password_length = 8

password = generate_password(password_length)
print(f"Generated password is: {password}")
```

## 43.A program that checks if a given string is a palindrome.
```python
def is_palindrome(s):
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
```

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
## 45.A program that sorts a list of numbers in ascending or descending order.
```python
List = [[2, 8, 10], [12, 45, 2], [4, 10, 1]]

# Ascending
print("Ascending:", sorted(List))

# Descending
print("Descending:", sorted(List, reverse=True))
```
## 47.Select query using MySQL and Python


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

