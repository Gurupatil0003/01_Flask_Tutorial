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

- The cursor() method in Python's MySQL  database connectivity, specifically with  libraries like mysql-connector-python, plays a  vital role in interacting with the database.  Here's a breakdown of its function:

- Creating a Cursor Object:

- When you call cursor() on a MySQL connection   object, it returns a cursor object. This object     acts as an intermediary between your Python  program and the MySQL server.
 Executing Database Operations:

- The cursor object allows you to execute  various database operations, primarily through  the execute() method. You can pass SQL statements (SELECT, INSERT, UPDATE, DELETE, etc.) to execute().
Fetching Results (for queries):

- If your SQL statement retrieves data (like a  SELECT query), the cursor object helps you  fetch the results one row at a time or in  batches. It provides methods like fetchone(),  fetchall(), etc., to retrieve data.


  ## 4.What is the Django admin console used for in a Django project?


Username: Guru 
Email address: guru@dummymail.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
My password did not meet the criteria, but this is a test environment, and I choose to create user anyway, by enter y:

Bypass password validation and create user anyway? [y/N]: y

If you press [Enter], you should have successfully created a user:

Superuser created successfully.

Now start the server again:

py manage.py runserver

In the browser window, type 127.0.0.1:8000/admin/ in the address bar.

<img src="https://github.com/Gurupatil0003/01_Flask_Tutorial/blob/main/Images/Screenshot%202024-03-25%20171440.png"  alt="structure" width="100%"  />

And fill in the form with the correct username and password:

<img src="https://github.com/Gurupatil0003/01_Flask_Tutorial/blob/main/Images/Screenshot%202024-03-25%20171504.png"  alt="structure" width="100%"  />

<img src="https://github.com/Gurupatil0003/01_Flask_Tutorial/blob/main/Images/Screenshot%202024-03-25%20171516.png"  alt="structure" width="100%"  />
