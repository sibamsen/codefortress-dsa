# 1021. Remove Outermost Parentheses

## Problem Understanding

Given a valid parentheses string `s`, remove the outermost parentheses from every primitive string.

### Example

Input:

```text
(()())(())
```

Primitive decomposition:

```text
(()()) + (())
```

After removing outermost parentheses:

```text
()() + ()
```

Output:

```text
()()()
```

---

# Algorithm Name

**Counter / Depth Tracking**

We maintain a variable:

```python
balance
```

which stores the number of currently active opening brackets.

---

# Algorithm Steps

### Step 1

Initialize:

```python
balance = 0
ans = ""
```

---

### Step 2

Traverse every character in the string.

```python
for ch in s:
```

---

### Step 3

If the current character is `'('`:

- If `balance > 0`, add it to the answer.
- Increase the balance.

```python
if ch == '(':

    if balance > 0:

        ans += ch

    balance += 1
```

---

### Step 4

If the current character is `')'`:

- Decrease the balance.
- If `balance > 0`, add it to the answer.

```python
else:

    balance -= 1

    if balance > 0:

        ans += ch
```

---

### Step 5

Return the answer.

```python
return ans
```

---

# How the Algorithm is Used in the Code

### Initialize variables

```python
balance = 0
ans = ""
```

---

### Traverse the string

```python
for ch in s:
```

---

### Handle opening bracket

```python
if ch == '(':

    if balance > 0:

        ans += ch

    balance += 1
```

---

### Handle closing bracket

```python
else:

    balance -= 1

    if balance > 0:

        ans += ch
```

---

### Return final answer

```python
return ans
```

---

# Complete Code

```python
class Solution:

    def removeOuterParentheses(self, s: str) -> str:

        balance = 0

        ans = ""

        for ch in s:

            if ch == '(':

                if balance > 0:

                    ans += ch

                balance += 1

            else:

                balance -= 1

                if balance > 0:

                    ans += ch

        return ans
```

---

# Dry Run

Input:

```text
(()())(())
```

Initial:

```python
balance = 0
ans = ""
```

| Character | Balance | Answer |
| ---------- | -------- | ------ |
| ( | 1 | "" |
| ( | 2 | ( |
| ) | 1 | () |
| ( | 2 | ()( |
| ) | 1 | ()() |
| ) | 0 | ()() |
| ( | 1 | ()() |
| ( | 2 | ()()( |
| ) | 1 | ()()() |
| ) | 0 | ()()() |

Final answer:

```text
()()()
```

---

# Time Complexity (Step by Step)

We traverse the string once:

```python
for ch in s:
```

If the length of the string is:

```text
n
```

The loop runs:

```text
n times
```

Therefore:

```text
Time Complexity = O(n)
```

---

# Space Complexity (Step by Step)

Extra variables:

```python
balance
```

takes:

```text
O(1)
```

The answer string stores at most `n` characters.

Therefore:

```text
Space Complexity = O(n)
```
