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

