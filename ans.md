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
