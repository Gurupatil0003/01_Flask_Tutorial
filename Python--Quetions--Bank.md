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
## 7.Python has a built-in **`open()`** function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.

## Syntax
<img src="https://github.com/Gurupatil0003/01_Flask_Tutorial/blob/main/Images/ReadOpen.png"  alt="structure" width="100%"  />

```python

f = open(\"test.txt\")
f = open("test.txt")   # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
```
## 8.What is the role of views in Django and how are they mapped to URLs?

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



