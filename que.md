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
