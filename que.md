```python
a = "developer"
b = "devel0perX"

max_len = max(len(a), len(b))

for i in range(max_len):
    ch1 = a[i] if i < len(a) else "-"
    ch2 = b[i] if i < len(b) else "-"
    
    if ch1 != ch2:
        print(f"Pos {i}: {ch1} != {ch2}")
```

```python
ip = "192.168.0.1"

parts = ip.split(".")
valid = True

if len(parts) != 4:
    valid = False
else:
    for p in parts:
        if not p.isdigit():
            valid = False
            break
        if not 0 <= int(p) <= 255:
            valid = False
            break
        if p != str(int(p)):  # no leading zeros
            valid = False
            break

print(valid)


```


```python

def final_position(commands):
    x = y = 0
    cmds = commands.split(";")

    for cmd in cmds:
        if not cmd.strip():
            continue

        direction, steps = cmd.strip().split()
        steps = int(steps)

        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps

    return (x, y)


print(final_position("UP 5; LEFT 3; DOWN 2; RIGHT 4"))


```

```python
sentence = "apple is an awesome idea but orange exists"
vowels = "aeiouAEIOU"

count = 0
for w in sentence.split():
    if w[0] in vowels:
        count += 1

print(count)


```

## #️⃣ 1. LIST – Important 10 Problems
1️⃣ Remove duplicates (keep order)
```python
arr = [2, 5, 2, 8, 5, 9]
seen = []
for x in arr:
    if x not in seen:
        seen.append(x)
print(seen)
```

2️⃣ Find second largest element
```python
arr = [10, 50, 20, 40]
arr2 = arr.copy()
arr2.remove(max(arr2))
print(max(arr2))
```

3️⃣ Move all zeros to end
```python
arr = [0, 3, 0, 2, 0, 9]
res = []
zero = 0

for x in arr:
    if x == 0:
        zero += 1
    else:
        res.append(x)

res += [0] * zero
print(res)
```
4️⃣ Merge two lists alternatively
```python
a = [1, 3, 5]
b = [2, 4, 6, 7]

i = 0
res = []

while i < len(a) or i < len(b):
    if i < len(a): res.append(a[i])
    if i < len(b): res.append(b[i])
    i += 1

print(res)
```

5️⃣ Count frequency of each number
```python
arr = [1, 2, 2, 3, 3, 3]
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

print(freq)

```
6️⃣ Reverse list without using reverse()
```python
arr = [1,2,3,4,5]
rev = []

for i in range(len(arr)-1, -1, -1):
    rev.append(arr[i])

print(rev)
```

7️⃣ Sum of even & odd numbers in list
```python
arr = [1, 2, 3, 4, 5, 6]
even = odd = 0

for x in arr:
    if x % 2 == 0:
        even += x
    else:
        odd += x

print(even, odd)
```

8️⃣ Remove adjacent duplicates
```python
arr = [1,1,2,2,3,1,1]
res = [arr[0]]

for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
        res.append(arr[i])

print(res)
```

9️⃣ Find common elements in two lists
```python
a = [1,2,3,4]
b = [3,4,5,6]
common = []

for x in a:
    if x in b:
        common.append(x)

print(common)
```

🔟 Find elements greater than average

```python
arr = [10, 20, 30, 40]
avg = sum(arr) / len(arr)

res = []
for x in arr:
    if x > avg:
        res.append(x)

print(res)

```

## tuple 

```python

t = (10, 20, 30, 40)
for i in range(len(t)):
    if t[i] == 30:
        print(i)
```
## 2️⃣ Find index of element
```python

t = (11,5,99,3)
mx = t[0]
mn = t[0]

for x in t:
    if x > mx: mx = x
    if x < mn: mn = x

print(mx, mn)


```

## dict

```python
1️⃣ Count Frequency of Each Word in a Sentence
Input
Sky is blue and the sky is clear

Expected Output
{'sky': 2, 'is': 2, 'blue': 1, 'and': 1, 'the': 1, 'clear': 1}
```
```python
sentence = "Sky is blue and the sky is clear"
sentence = sentence.lower().split()

freq = {}

for word in sentence:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)

```

```python
3️⃣ Reverse Keys and Values
Input
{'a': 1, 'b': 2, 'c': 3}

Output
{1: 'a', 2: 'b', 3: 'c'}

✅ Code
d = {'a': 1, 'b': 2, 'c': 3}

rev = {}
for k, v in d.items():
    rev[v] = k

print(rev)


```
6️⃣ Character Frequency Without Using Counter
Input
"success"

Output
{'s': 3, 'u': 1, 'c': 2, 'e': 1}

✅ Code
s = "success"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)
```
## palidrome
```python
a="12trt1"

b=a[::-1]

if a==b:
    print("is aplidrome")
else:
    print("no")
```

## 6️⃣ Check if two strings are anagrams
```
a = "listen"
b = "silent"

if sorted(a.lower()) == sorted(b.lower()):
    print(True)
else:
    print(False)

```
## 4️⃣ Count uppercase, lowercase, digits, and spaces

```python
s = "Cts 2026 GenC"
upper = lower = digit = space = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif ch == " ":
        space += 1

print(upper, lower, digit, space)


```

## 2️⃣ Count vowels and consonants

```python
s = "cognizant"
vowels = "aeiouAEIOU"
v_count = c_count = 0

for ch in s:
    if ch in vowels:
        v_count += 1
    else:
        c_count += 1

print("Vowels:", v_count, "Consonants:", c_count)

```
## Loops
## 1️⃣ Print numbers from 1 to 10
```python
for i in range(1, 11):
    print(i, end=" ")
```
## 2️⃣ Print even numbers between 1 to 50
```python
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
```

## 3️⃣ Sum of first N natural numbers
```python
N = 10
total = 0

for i in range(1, N+1):
    total += i

print(total)

```

## 5️⃣ Fibonacci series up to N terms
```python
N = 7
a, b = 0, 1

for i in range(N):
    print(a, end=" ")
    a, b = b, a+b
```

## function

```python

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(7))


```
```python
def validate_password(pwd):
    if len(pwd) > 8:
        print("Valid")
    else:
        print("Invalid")

validate_password("CTS2026")
validate_password("StrongPassword")


```
## Oops
```python
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(self.name, "balance:", self.balance)


# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(300)
account.show_balance()
```

```python
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  # List of marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(self.name, "Roll No:", self.roll_no)
        print("Average marks:", self.average_marks())


# Usage
student = Student("Bob", 101, [80, 90, 85])
student.display()
```

```python
class Cat:
    def mood(self): 
       print("Grumpy") 
    def sound(self): 
       print("Meow") 
 
class Dog:
    def mood(self): 
       print("Happy") 
    def sound(self): 
       print("Woof") 
 
hello_kitty = Cat()
hello_puppy = Dog()
 
for pet in (hello_kitty, hello_puppy):
    pet.mood()
    pet.sound()

```

