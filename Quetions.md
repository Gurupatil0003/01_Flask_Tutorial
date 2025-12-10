# 🧮 List Manipulation Problems  

Below are eight problems involving list operations. Follow the input/output specifications and constraints provided.

---

## **1️⃣ Remove Duplicates (Keep Order)**

### **Problem**
Given a list of integers, remove all duplicate elements **while preserving the original order**.

### **Input Format**
- A single line containing space-separated integers.

### **Output Format**
- A list with duplicates removed in the same order as the first occurrence.

### **Constraints**
- `1 ≤ N ≤ 10^5`
- Integers may be negative.

### **Example**
**Input:**  
`1 2 2 3 1 4`  
**Output:**  
`[1, 2, 3, 4]`

---

## **2️⃣ Find the Second Largest Element**

### **Problem**
Given a list of integers, find the **second largest distinct value**.

### **Input Format**
- A single line of space-separated integers.

### **Output Format**
- A single integer (second largest).  
- If not possible, print: `Not enough distinct elements`

### **Constraints**
- `2 ≤ N ≤ 10^5`

### **Example**
**Input:**  
`10 20 4 5 20`  
**Output:**  
`10`

---

## **3️⃣ Move All Zeros to the End**

### **Problem**
Rearrange the list such that **all zeros move to the end**, while maintaining the order of non-zero elements.

### **Input Format**
- A single line of space-separated integers.

### **Output Format**
- List with zeros moved to the end.

### **Constraints**
- `1 ≤ N ≤ 10^5`

### **Example**
**Input:**  
`0 1 0 3 12`  
**Output:**  
`[1, 3, 12, 0, 0]`

---

## **4️⃣ Merge Two Lists Alternately**

### **Problem**
Given two lists, merge them by taking elements **alternatively** from each.  
If one list is longer, append the remaining elements at the end.

### **Input Format**
- Line 1: List A (space-separated)  
- Line 2: List B (space-separated)

### **Output Format**
- Alternately merged list.

### **Constraints**
- `1 ≤ len(A), len(B) ≤ 10^5`

### **Example**
**Input:**  
1 2 3
4 5 6 7 8

**Output:**  
`[1, 4, 2, 5, 3, 6, 7, 8]`

---

## **5️⃣ Count Frequency of Each Number**

### **Problem**
Count how many times each unique number appears in the list.

### **Input Format**
- A single line of space-separated integers.

### **Output Format**
- Print number → frequency pairs (order by first occurrence).

### **Constraints**
- `1 ≤ N ≤ 10^5`

### **Example**
**Input:**  
`4 5 4 6 5 4`  
**Output:**  
4 → 3
5 → 2
6 → 1


---

## **6️⃣ Reverse List Without Using `reverse()`**

### **Problem**
Given a list, reverse it manually **without using built-in reverse functions**.

### **Input Format**
- A single line of space-separated integers.

### **Output Format**
- Reversed list.

### **Constraints**
- `1 ≤ N ≤ 10^5`

### **Example**
**Input:**  
`10 20 30 40`  
**Output:**  
`[40, 30, 20, 10]`

---

## **7️⃣ Sum of Even & Odd Numbers**

### **Problem**
Find the **sum of all even numbers** and **sum of all odd numbers** in the list.

### **Input Format**
- A single line of space-separated integers.

### **Output Format**
- Two integers:  
`even_sum odd_sum`

### **Constraints**
- `1 ≤ N ≤ 10^5`

### **Example**
**Input:**  
`1 2 3 4 5`  
**Output:**  
`6 9`

---

## **8️⃣ Remove Adjacent Duplicates**

### **Problem**
Remove only consecutive duplicate elements.

### **Input Format**
- A single line of space-separated integers.

### **Output Format**
- List with adjacent duplicates removed.

### **Constraints**
- `1 ≤ N ≤ 10^5`

### **Example**
**Input:**  
`1 1 2 2 2 3 1 1`  
**Output:**  
`[1, 2, 3, 1]`

---


# 🧮 Additional List, Tuple & Dictionary Problems

Below are newly added problems with input/output format and constraints.

---

## **9️⃣ Find Common Elements in Two Lists**

### **Problem**
Given two lists, find all the **common elements** between them.

### **Input Format**
- Line 1: List A (space-separated integers)  
- Line 2: List B (space-separated integers)

### **Output Format**
- A list containing common elements (no duplicates).

### **Constraints**
- `1 ≤ len(A), len(B) ≤ 10^5`

### **Example**
**Input:**  
1 2 3 4
3 4 5 6

**Output:**  
`[3, 4]`

---

## **🔟 Find Elements Greater Than Average**

### **Problem**
Given a list of integers, find all elements **greater than the average** value of the list.

### **Input Format**
- A single line of space-separated integers.

### **Output Format**
- A list of numbers greater than the average.

### **Constraints**
- `1 ≤ N ≤ 10^5`

### **Example**
**Input:**  
`1 2 3 4 5 6`  
**Output:**  
`[4, 5, 6]`

---

# 🟣 Tuple Problems

---

## **1️⃣ Find Index of Element (Tuple)**

### **Problem**
Given a tuple and an element, find the **index** of the element.

### **Input Format**
- Line 1: Tuple elements (space-separated)  
- Line 2: Element to search

### **Output Format**
- Index of the element  
- If not found: `Element not found`

### **Constraints**
- `1 ≤ N ≤ 10^5`

### **Example**
**Input:**  
10 20 30 40 50
30

**Output:**  
`2`

---

## **2️⃣ Finding Minimum and Maximum in Tuple**

### **Problem**
Given a tuple, find the **minimum** and **maximum** elements.

### **Input Format**
- A single line of space-separated integers.

### **Output Format**
- Two integers: `min max`

### **Example**
**Input:**  
`4 7 1 9 3`  
**Output:**  
`1 9`

---

# 🟡 Dictionary Problems

---

## **1️⃣ Count Frequency of Each Word in a Sentence**

### **Problem**
Given a sentence, count how many times each word appears (**case-insensitive**).

### **Input Format**
- A string (sentence)

### **Output Format**
- A dictionary containing word → frequency

### **Example**
**Input:**  
`Sky is blue and the sky is clear`

**Output:**  
`{'sky': 2, 'is': 2, 'blue': 1, 'and': 1, 'the': 1, 'clear': 1}`

---

## **3️⃣ Reverse Keys and Values**

### **Problem**
Given a dictionary, reverse it so that **values become keys** and **keys become values**.

### **Input Format**
- A dictionary (string format)

### **Output Format**
- Reversed dictionary

### **Example**
**Input:**  
`{'a': 1, 'b': 2, 'c': 3}`  

**Output:**  
`{1: 'a', 2: 'b', 3: 'c'}`

---


# 🔤 String, Loop & Math Problems

Below are additional problems with input/output format and constraints.

---

# 🟣 String Problems

---

## **1️⃣ Character Frequency Without Using Counter**

### **Problem**
Given a string, count the frequency of each character **without** using `collections.Counter`.

### **Input Format**
- A single string

### **Output Format**
- Dictionary of character → count

### **Example**
**Input:**  
`hello world`  
**Output:**  
`{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}`

---

## **2️⃣ Count Vowels and Consonants**

### **Problem**
Count how many vowels and consonants are present in a string.

### **Input Format**
- A single string

### **Output Format**
- `vowels consonants`

### **Example**
**Input:**  
`hello`  
**Output:**  
`2 3`

---

## **3️⃣ Check if String is Palindrome**

### **Problem**
Check whether the given string reads the same forward and backward.

### **Input Format**
- A single string

### **Output Format**
- `Palindrome` or `Not Palindrome`

### **Example**
**Input:**  
`madam`  
**Output:**  
`Palindrome`

---

## **4️⃣ Check if Two Strings Are Anagrams**

### **Problem**
Two strings are anagrams if they contain the same characters in any order.

### **Input Format**
- Line 1: String A  
- Line 2: String B

### **Output Format**
- `Anagram` or `Not Anagram`

### **Example**
**Input:**  
listen
silent

**Output:**  
`Anagram`

---

## **5️⃣ Count Uppercase, Lowercase, Digits, and Spaces**

### **Problem**
Given a string, count the number of uppercase letters, lowercase letters, digits, and spaces.

### **Input Format**
- A single string

### **Output Format**
- `uppercase lowercase digits spaces`

### **Example**
**Input:**  
`Hello World 123`  
**Output:**  
`2 8 3 2`

---

---

# 🔢 Loop & Math Problems

---

## **1️⃣ Print Numbers from 1 to 10**

### **Problem**
Print all numbers from 1 to 10.

### **Output Format**
- Numbers printed in a single line.

### **Example**
**Output:**  
`1 2 3 4 5 6 7 8 9 10`

---

## **2️⃣ Print Even Numbers Between 1 to 50**

### **Problem**
Print all even numbers from 1 to 50.

### **Output Format**
- Space-separated even numbers.

### **Example**
**Output:**  
`2 4 6 8 ... 50`

---

## **3️⃣ Sum of First N Natural Numbers**

### **Problem**
Given `N`, find the sum of the first `N` natural numbers.

### **Input Format**
- A single integer `N`

### **Output Format**
- A single integer (sum)

### **Example**
**Input:**  
`5`  
**Output:**  
`15`

---

## **4️⃣ Fibonacci Series Up to N Terms**

### **Problem**
Print the Fibonacci sequence up to `N` terms.

### **Input Format**
- A single integer `N`

### **Output Format**
- Fibonacci numbers in a list

### **Example**
**Input:**  
`7`  
**Output:**  
`[0, 1, 1, 2, 3, 5, 8]`

---

## **5️⃣ Factorial of a Number**

### **Problem**
Given a number `N`, compute its factorial.

### **Input Format**
- A single integer `N`

### **Output Format**
- Factorial value

### **Example**
**Input:**  
`5`  
**Output:**  
`120`

---

# 🧩 Object-Oriented Programming (OOP) & Additional Problems

Below are OOP-based mini-projects and extra coding questions with proper structure and explanations.

---

# 🟦 OOP Projects / Scenarios

---

## **1️⃣ Bank Management System (OOP)**

### **Problem**
Create a `BankAccount` class with:
- Attributes: `name`, `account_number`, `balance`
- Methods:
  - `deposit(amount)`
  - `withdraw(amount)`
  - `check_balance()`

### **Expected Output**
When methods are called, proper transaction messages and updated balances should be shown.

---

## **2️⃣ School Management System (OOP)**

### **Problem**
Create two classes:  
- `Student` → name, roll number, marks  
- `Teacher` → name, subject  

Functions:
- Add student  
- Add teacher  
- Display information  

### **Expected Output**
Objects must print details in a formatted way.

---

## **3️⃣ Polymorphism Example – Dog & Cat Sounds**

### **Problem**
Create a base class `Animal` with a method `sound()`.  
Create subclasses:
- `Dog` → returns `"Bark!"`
- `Cat` → returns `"Meow!"`

### **Expected Output**
Calling:
animal_sound( Dog() )
animal_sound( Cat() )

Should print:
Bark!
Meow!


---

# 🟧 String Problems

---

## **1️⃣ First Non-Repeating Character**

### **Problem**
Given a string, return the first character that does not repeat.

### **Input Format**
- A single string

### **Output Format**
- One character  
- If none: `No unique character`

### **Example**
**Input:**  
`swiss`  
**Output:**  
`w`

---

## **2️⃣ Remove Duplicates (Preserve Order)**

### **Problem**
Remove all repeated characters but keep the first occurrence.

### **Input Format**
- A single string

### **Output Format**
- String after removing duplicates

### **Example**
**Input:**  
`banana`  
**Output:**  
`ban`

---

## **3️⃣ Rotate String by K**

### **Problem**
Rotate a string right by `K` positions.

### **Input Format**
- Line 1: String  
- Line 2: Integer K

### **Output Format**
- Rotated string

### **Example**
**Input:**  
hello
2
**Output:**  
`lohel`

---

## **4️⃣ Password Validation**

### **Problem**
A password is valid if:
- At least 8 characters  
- Contains uppercase  
- Contains lowercase  
- Contains digit  
- Contains special character  

### **Input Format**
- A single string (password)

### **Output**
- `Valid Password` or `Invalid Password`

### **Example**
**Input:**  
`Pass@123`  
**Output:**  
`Valid Password`

---

## **5️⃣ Count “Special Substrings” (First & Last Char Same)**

### **Problem**
Count all substrings where the **first and last characters are the same**.

### **Input Format**
- A single string

### **Output Format**
- Integer count

### **Example**
**Input:**  
`abcab`  
**Output:**  
`7`

(Explanation: a, b, c, a, b, aba, bab)

---

# 🟨 Math & Logic Problems

---

## **1️⃣ GCD (Greatest Common Divisor)**

### **Problem**
Given two integers, compute the GCD using the Euclidean algorithm.

### **Input Format**
- Two integers

### **Output**
- GCD value

### **Example**
**Input:**  
`20 8`  
**Output:**  
`4`

---

## **2️⃣ Leap Year Check**

### **Problem**
Determine if a year is a leap year.

### **Rules**
A year is leap if:
- divisible by 4  
- NOT divisible by 100  
- OR divisible by 400  

### **Input Format**
- Integer year

### **Output**
- `Leap Year` or `Not Leap Year`

### **Example**
**Input:**  
`2024`  
**Output:**  
`Leap Year`

---



````````````````````````


1️⃣ Remove duplicates (keep order)

2️⃣ Find second largest element 3️⃣
Move all zeros to end 
4️⃣ Merge two lists alternatively 
5️⃣ Count frequency of each number 
6️⃣ Reverse list without using reverse() 
7️⃣ Sum of even & odd numbers in list 
8️⃣ Remove adjacent duplicates 
9️⃣ Find common elements in two lists 
🔟 Find elements greater than average 
tuple section
2️⃣ Find index of element finding min and max

1️⃣ Count Frequency of Each Word in a Sentence
Input
Sky is blue and the sky is clear

Expected Output
{'sky': 2, 'is': 2, 'blue': 1, 'and': 1, 'the': 1, 'clear': 1}

3️⃣ Reverse Keys and Values
Input
{'a': 1, 'b': 2, 'c': 3}

Output
{1: 'a', 2: 'b', 3: 'c'}
6️⃣ Character Frequency Without Using Counter

palidrome
6️⃣ Check if two strings are anagrams
4️⃣ Count uppercase, lowercase, digits, and spaces

2️⃣ Count vowels and consonants
1️⃣ Print numbers from 1 to 10
2️⃣ Print even numbers between 1 to 50
3️⃣ Sum of first N natural numbers

5️⃣ Fibonacci series up to N terms
factorial

oops section
bank mangement
school mangement
polymorphism sound and mood of dog and cat wn i call ill get two sound output
5. First non-repeating character
Remove duplicates (preserve order)
Rotate string by K
5. Password validation
Count “special substrings” (first & last char same)
gcd 
leap year



