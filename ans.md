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

