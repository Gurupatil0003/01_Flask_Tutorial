# Unit 1: Python Basics - Questions and Answers

## 1. Identifiers and Operators

### Identifiers:
Identifiers are names used to identify variables, functions, classes, modules, etc.
- Must start with a letter (A-Z, a-z) or an underscore (_)
- Can contain letters, digits, and underscores
- Cannot use keywords like `for`, `if`, `else`, `class`, etc.
- Are case-sensitive: `Name` and `name` are different.

### Operators:
Operators are symbols that perform operations on variables and values.

| Type              | Operators                             | Example         |
|-------------------|----------------------------------------|-----------------|
| **Arithmetic**        | `+`, `-`, `*`, `/`, `//`, `%`, `**`    | `a + b`         |
| **Comparison**        | `==`, `!=`, `>`, `<`, `>=`, `<=`       | `a > b`         |
| **Logical**           | `and`, `or`, `not`                     | `a > b and b > c` |
| **Assignment**        | `=`, `+=`, `-=`, `*=`, `/=`, etc.      | `x += 2`        |
| **Bitwise**           | `&`, `|`, `^`, `~`, `<<`, `>>`         | `a & b`         |
| **Membership**        | `in`, `not in`                         | `'a' in 'apple'`|
| **Identity**          | `is`, `is not`                         | `a is b`        |

---

## 2. Variables and Naming Rules

### Variables:
Variables are containers for storing data values.

Example:
```python
name = "Guru"
age = 25
```

# Python Basics - Naming Rules and Data Types

## 1. Naming Rules

- **Must start with a letter or underscore**  
- **Cannot start with a digit**  
- **Can contain letters, numbers, and underscores**  
- **Cannot be a keyword**  
- **Are case-sensitive**  

---

## 2. Data Types

Python has the following built-in data types:

| **Type**     | **Example**                           | **Description**                  |
|--------------|---------------------------------------|----------------------------------|
| **int**      | `x = 10`                              | Integer                         |
| **float**    | `y = 5.5`                             | Decimal (floating point)        |
| **bool**     | `True`, `False`                       | Boolean                         |
| **str**      | `"hello"`                             | String                          |
| **list**     | `fruits = ["apple", "banana"]`        | Mutable ordered collection      |
| **tuple**    | `days = ("Mon", "Tue", "Wed")`        | Immutable ordered collection    |
| **set**      | `nums = {1, 2, 3}`                    | Unordered unique elements       |
| **dict**     | `person = {"name": "Guru", "age": 25}`| Key-value pairs                 |
| **complex**  | `z = 2 + 3j`                          | Complex numbers                 |
| **range**    | `range(5)`                            | Sequence from 0 to 4            |

---

## 3. List, Tuple, Set, Dictionary, String, Range

- **List**: Mutable, ordered  
  Example: `fruits = ["apple", "banana"]`
  
- **Tuple**: Immutable, ordered  
  Example: `days = ("Mon", "Tue", "Wed")`

- **Set**: Mutable, unordered, unique elements  
  Example: `nums = {1, 2, 2, 3}`

- **Dictionary**: Key-value pairs  
  Example: `person = {"name": "Guru", "age": 25}`

- **String**: Text data  
  Example: `name = "Python"`

- **Range**: Generates sequence of numbers  
  Example: 
  ```python
  for i in range(5):
      print(i)
```

# Python Basics - Conditional Statements, Loops, and Functions

## 5. Conditional Statements (`if`, `elif`, `else`)

Used to perform different actions based on conditions.

### Example:

```python
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

# Python Basics - Loops and Functions

## 6. Loops (`for` and `while`)

### `for` loop:
Used to iterate over sequences like lists, strings, etc.

### Example:

```python
for i in range(3):
    print(i)
```

### while loop:
Runs as long as the condition is True.

Example:
``` python

i = 0
while i < 3:
    print(i)
    i += 1
```

## 7. Built-in Functions vs User-defined Functions

### Built-in Functions:
Predefined functions provided by Python.  
Examples: `print()`, `len()`, `type()`, `input()`

### User-defined Functions:
Functions created by users using the `def` keyword.

### Example:

```python
def greet(name):
    return "Hello " + name

print(greet("Guru"))  # Output: Hello Guru
```

# Unit 2

## 2. What is `lambda` and `def` function?

### `def` Function:
A `def` function is a normal function created using the `def` keyword. It can take arguments, perform tasks, and return a value.

#### Syntax:

```python
def function_name(arguments):
    # function body
    return result
```
Example of def function:
``` python

def greet(name):
    return "Hello, " + name

print(greet("Guru"))  # Output: Hello, Guru

```

## Lambda Function

A lambda function is an anonymous function defined using the `lambda` keyword. It can have any number of arguments but only one expression. Lambda functions are commonly used for short-term operations or as arguments to higher-order functions like `map()`, `filter()`, and `reduce()`.

### Syntax:

```python
lambda arguments: expression
```
# Example
```
multiply = lambda x, y: x * y
print(multiply(3, 5))  # Output: 15
```

## Global and Local Variables with Examples

### Global Variables:
A global variable is a variable that is defined outside of any function. It can be accessed from anywhere in the program, both inside and outside functions.

### Example of Global Variable:

```python
name = "Guru"  # Global variable

def greet():
    print("Hello, " + name)  # Accessing global variable

greet()  # Output: Hello, Guru
```

## Local Variables and Function Arguments

### Local Variables:
A local variable is a variable that is defined inside a function. It is only accessible within that function and cannot be accessed outside of it.

### Example of Local Variable:

```python
def greet():
    name = "Guru"  # Local variable
    print("Hello, " + name)

greet()  # Output: Hello, Guru
# print(name)  # This will give an error because `name` is a local variable
```

### Function Arguments:
Function arguments are values passed to a function when it is called. They are used to pass information into the function for processing.

### Example with Arguments:
```python
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Guru", 25)  # Output: Hello, Guru! You are 25 years old.

```

## Functions with Return Value

Functions can return a value to the caller using the `return` keyword. The returned value can be assigned to a variable, printed, or used in any other expression.

### Example of Function with Return Value:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

## 4. What is OOPs Function and its Concept

### OOPs (Object-Oriented Programming) Functions:
In Object-Oriented Programming (OOP), functions are typically defined inside classes and are known as methods. These methods operate on data contained within the object and can perform actions related to that object.

### Key Concepts of OOP:
1. **Class**: A blueprint for creating objects (a collection of attributes and methods).
2. **Object**: An instance of a class.
3. **Inheritance**: The ability to create a new class based on an existing class.
4. **Polymorphism**: The ability to use a method in different ways.
5. **Abstraction**: Hiding the complexity of the system and showing only the necessary parts.
6. **Encapsulation**: Binding the data (attributes) and methods together inside a class and restricting access to them.

### Example of OOPs Function:

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name  # Attribute
        self.sound = sound  # Attribute

    def make_sound(self):  # Method (OOP function)
        return f"The {self.name} says {self.sound}"

# Create an object (instance) of the class Animal
dog = Animal("Dog", "Bark")
cat = Animal("Cat", "Meow")

print(dog.make_sound())  # Output: The Dog says Bark
print(cat.make_sound())  # Output: The Cat says Meow
```

## 6. File Handling or Working with Files

File handling is an essential aspect of Python programming. Python provides several built-in functions and methods to work with files, including reading, writing, and manipulating files. You can open, read, write, and close files using Python's built-in functions.

### File Modes
Python uses different modes to open files. Here are the most commonly used modes:

- `"r"`: **Read mode** (default mode) – Opens the file for reading.
- `"w"`: **Write mode** – Opens the file for writing. If the file doesn't exist, a new file is created. If the file exists, it truncates the file.
- `"a"`: **Append mode** – Opens the file for writing. If the file doesn't exist, a new file is created. It appends data to the end of the file if the file already exists.
- `"b"`: **Binary mode** – Opens the file in binary mode (useful for non-text files like images).

---

### Reading from a File
Once a file is opened in **read mode** (`"r"`), you can read its contents using methods like `read()`, `readline()`, and `readlines()`.

#### Example of Reading the Entire File:
```python
# Open the file in read mode
file = open("example.txt", "r")

# Read the entire content of the file
content = file.read()
print(content)

# Close the file
file.close()
```
## 7. Exception Handling (try, except, finally, and else)

Exception handling is a mechanism in Python that allows us to deal with runtime errors, preventing the program from crashing. Python provides a set of keywords to handle exceptions: `try`, `except`, `finally`, and `else`.

### `try` Block
The `try` block is used to define a block of code that might raise an exception. If an exception occurs, Python stops executing the code in the `try` block and moves to the `except` block.

### `except` Block
The `except` block catches the exception raised in the `try` block. You can specify the type of exception you want to catch or catch any exception in general.

### `finally` Block
The `finally` block contains code that will be executed no matter what, whether an exception occurs or not. It is commonly used to perform cleanup operations, such as closing files or releasing resources.

### `else` Block
The `else` block is optional. It will execute only if no exception occurs in the `try` block. It is used when you want to perform an action only if the `try` block runs successfully without exceptions.

---

### Example of Exception Handling:

```python
try:
    # Code that might raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    # Code to handle division by zero
    print("Error: Cannot divide by zero!")
except ValueError:
    # Code to handle invalid input
    print("Error: Invalid input. Please enter a number.")
else:
    # Code to execute if no exceptions occur
    print("Result is:", result)
finally:
    # Code that will always execute
    print("Execution completed.")
```

## Recursion

**Recursion** is a programming concept where a function calls itself in order to solve a problem. This technique is often used to solve problems that can be broken down into smaller, similar sub-problems.

In a recursive function, there are typically two main components:
1. **Base Case**: The condition that stops the recursion. Without a base case, the recursion will continue indefinitely.
2. **Recursive Case**: The part of the function where it calls itself with modified arguments.

### Example of Recursion

Let's take an example of calculating the factorial of a number using recursion.

**Factorial** of a number `n` is defined as:
- `n! = n * (n-1) * (n-2) * ... * 1`
- The base case is `0! = 1`.

Here's a Python example of how recursion works for calculating a factorial:

```python
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)

# Test the function
result = factorial(5)
print(result)  # Output: 120
```

# Unit 3

# Modules, Packages, and Libraries in Python

## 1. Modules

A **module** in Python is a file containing Python code that can define functions, classes, and variables. It can also include runnable code. Modules allow you to break down large programs into smaller, manageable, and organized files. 

### Importing a Module:
You can import a module into your Python script using the `import` keyword. Once imported, you can access the functions and variables defined within the module.

```python
# Import the math module
import math

# Use the sqrt function from the math module
result = math.sqrt(16)
print(result)  # Output: 4.0
```

### Creating Your Own Module

To create a module, simply save a Python file with the `.py` extension, and you can import it into other programs.

#### Example:

If you have a file `my_module.py` with the following content:

```python
# my_module.py
def greet(name):
    return "Hello, " + name
```

### 2. Packages

A package is a collection of modules organized in directories. A package typically contains multiple modules (Python files) grouped together under a common directory.

#### Creating a Package:

To create a package, organize the Python files (modules) in a directory and include an `__init__.py` file to mark the directory as a package. The `__init__.py` file can be empty or contain initialization code for the package.

#### Example of a Package Structure:
``` python
my_package/
    __init__.py
    module1.py
    module2.py
```

- `my_package/` is the main package directory.
- `__init__.py` is the file that tells Python to treat this directory as a package.
- `module1.py` and `module2.py` are modules within the package.

#### Importing and Using a Module from a Package:

To import and use a module from a package:

```python
from my_package import module1

module1.some_function()
```

## 3. Libraries

A **library** is a collection of pre-written code (modules and packages) that you can use in your program to avoid reinventing the wheel. Python has a rich standard library, but you can also install **third-party libraries** to extend Python's functionality.

---

### 📚 Examples of Popular Python Libraries:

#### 🔬 Data Science Libraries:
- **NumPy**: For numerical computations.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For creating static, animated, and interactive visualizations.

#### 🌐 Web Development Libraries:
- **Flask**: A micro web framework for building web applications.
- **Django**: A high-level web framework for rapid web development.

#### 🤖 Machine Learning Libraries:
- **Scikit-learn**: For machine learning algorithms and tools.
- **TensorFlow**: For deep learning and neural network models.
- **Keras**: A high-level neural networks API.

---

### 📦 Installing and Using External Libraries

You can install external libraries using `pip`, Python's package manager.

``` bash
pip install numpy
```

``` python
import numpy as np

arr = np.array([1, 2, 3])
print(arr)  # Output: [1 2 3]

```

#### ✅ Advantages of Using Libraries:
Efficiency: Libraries help save time by offering pre-built solutions for common problems.

Reusability: Libraries allow you to reuse code and extend functionality without starting from scratch.

Community Support: Popular libraries often have large communities and documentation, making them easier to use.


## Git and PyCharm Version Integration

### ✅ Prerequisites

- **Git Installed**  
  Make sure Git is installed on your system. You can verify this by running:
  ```bash
  git --version
  ```

PyCharm Installed
Ensure you're using a recent version of PyCharm (Community or Professional edition).

🔧 Configuring Git in PyCharm
Open PyCharm.

Go to File > Settings (or PyCharm > Preferences on macOS).

Navigate to Version Control > Git.

In the Path to Git executable, provide the correct Git path:

Windows: C:\Program Files\Git\bin\git.exe

macOS/Linux: Just use git (if it's in the system PATH)

Click the Test button to check if Git is detected.

Click OK to save the settings.

✅ Verifying Git Version in PyCharm
Go to VCS > Git > Show Git Log to view commit history.

Or open the Terminal tab in PyCharm and run:

``` bash

git --version

```


# 🐍 Python Connectivity with MySQL

This guide demonstrates how to connect Python with a MySQL database using the `mysql-connector-python` library.

---

## ✅ Prerequisites

- Python installed (3.x recommended)
- MySQL Server installed and running
- MySQL user credentials (username, password)
- Install MySQL connector:

```bash
pip install mysql-connector-python
```

## 🔗 Connecting to MySQL Database
## 📌 Basic Connection Example

``` python

import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM your_table")

# Fetch results
results = cursor.fetchall()

# Print results
for row in results:
    print(row)

# Close the connection
cursor.close()
conn.close()
🛠️ Create Database and Table
python
Copy
Edit
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS sample_db")
cursor.execute("USE sample_db")
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")

conn.commit()
cursor.close()
conn.close()
```

# 🍃 Python with MongoDB - CRUD Operations

This guide demonstrates how to perform **Create**, **Read**, **Update**, and **Delete (CRUD)** operations using **Python** and **MongoDB** via the `pymongo` library.

---

## ✅ Prerequisites

- MongoDB installed and running locally or on the cloud (e.g., MongoDB Atlas)
- Python 3.x installed
- Install PyMongo:

```bash
pip install pymongo
```

``` python
# Importing pymongo
from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Default host and port
db = client["mydatabase"]                          # Create or connect to a database
collection = db["students"]                        # Create or connect to a collection

# Step 2: Create (Insert documents)
student1 = {"name": "Guru", "age": 25, "course": "Python"}
student2 = {"name": "Mounesh", "age": 24, "course": "JavaScript"}
collection.insert_one(student1)
collection.insert_one(student2)

print("✅ Inserted documents.")

# Step 3: Read (Retrieve documents)
print("\n📖 All Students:")
for student in collection.find():
    print(student)

# Step 4: Update (Modify documents)
query = {"name": "Guru"}
new_values = {"$set": {"age": 26}}
collection.update_one(query, new_values)

print("\n🔄 Updated Guru's age:")
print(collection.find_one({"name": "Guru"}))

# Step 5: Delete (Remove documents)
delete_query = {"name": "Mounesh"}
collection.delete_one(delete_query)

print("\n❌ Deleted Mounesh. Remaining documents:")
for student in collection.find():
    print(student)

# Optional: Drop the collection (cleanup)
# collection.drop()
```

# Pytest Explanation with Example

## What is Pytest?

**Pytest** is a testing framework for Python that makes it easy to write simple as well as scalable test cases. It is used to ensure the correctness of your code and allows you to perform unit testing, integration testing, and functional testing.

### Advantages of Using Pytest:
- Simple syntax and powerful features
- Supports fixtures and parameterized testing
- Works with existing tests and test suites
- Provides detailed error messages
- Supports integration with continuous integration tools

## Installation

You can install pytest using `pip`:

```bash
pip install pytest
```

# Pytest Example for Calculator

## Example: `calculator.py`

This file contains the functions to be tested.

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

# Create a Test File Using Pytest
In this step, we create a test file that uses pytest to test the functions in calculator.py.

## Example: test_calculator.py
``` python
# test_calculator.py
import pytest
from calculator import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2
Running the Tests
To run the tests, use the following command in the terminal:
```

``` python
pytest test_calculator.py
```

## Output
When you run pytest on the test file, it will output the results:

``` pytohn 
$ pytest test_calculator.py
==================== test session starts ====================
collected 2 items

test_calculator.py ..                                      [100%]

===================== 2 passed in 0.03 seconds =================
```
