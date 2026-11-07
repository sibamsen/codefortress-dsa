# LeetCode 412: Fizz Buzz

## 1. Problem Statement

Given an integer `n`, return a string array `answer` (1-indexed) where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by both 3 and 5.
- `answer[i] == "Fizz"` if `i` is divisible by 3.
- `answer[i] == "Buzz"` if `i` is divisible by 5.
- `answer[i] == str(i)` if none of the above conditions are true.

In simple words, traverse numbers from `1` to `n` and replace numbers according to their divisibility.

### Example

**Input:**
```python
n = 5
```

**Output:**
```python
["1", "2", "Fizz", "4", "Buzz"]
```

**Explanation:**

- 1 → Neither divisible by 3 nor 5 → `"1"`
- 2 → Neither divisible by 3 nor 5 → `"2"`
- 3 → Divisible by 3 → `"Fizz"`
- 4 → Neither divisible by 3 nor 5 → `"4"`
- 5 → Divisible by 5 → `"Buzz"`

---

## 2. Approach / Algorithm Name

**Brute Force / Linear Traversal with Conditional Statements**

### Algorithm Steps

1. Create an empty list `ans`.
2. Traverse numbers from `1` to `n` using a loop.
3. Check whether the current number is divisible by both 3 and 5.
   - If true, append `"FizzBuzz"`.
4. Otherwise, check whether it is divisible by 3.
   - If true, append `"Fizz"`.
5. Otherwise, check whether it is divisible by 5.
   - If true, append `"Buzz"`.
6. If none of the conditions are satisfied, append the number after converting it into a string using `str(i)`.
7. Return the resulting list.

**Important:** Always check divisibility by both 3 and 5 first.

---

## 3. Time and Space Complexity

### Time Complexity: O(n)

- The loop runs from `1` to `n`, executing `n` iterations.
- Each iteration performs a constant number of divisibility checks and one append operation.
- Therefore, each iteration takes `O(1)` time.

Total:

`n × O(1) = O(n)`

### Space Complexity: O(n)

- An answer list is created to store `n` strings.
- Therefore, the output list requires `O(n)` space.
- Excluding the output list, the auxiliary space is `O(1)`.

**Overall Space Complexity = O(n)** including the output.

---

## 4. Code

```python
class Solution:
    def fizzBuzz(self, n):

        ans = []

        for i in range(1, n + 1):

            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")

            elif i % 3 == 0:
                ans.append("Fizz")

            elif i % 5 == 0:
                ans.append("Buzz")

            else:
                ans.append(str(i))

        return ans
```

---

## 5. Driver Code

```python
if __name__ == "__main__":

    n = int(input("Enter n: "))

    sol = Solution()

    result = sol.fizzBuzz(n)

    print("Fizz Buzz Output:", result)
```

---

## 6. Output

**Input:**
```text
Enter n: 5
```

**Output:**
```text
Fizz Buzz Output: ['1', '2', 'Fizz', '4', 'Buzz']
```

### Dry Run

For `n = 5`:

| i | Condition | Appended Value |
|---|---|---|
| 1 | Neither divisible by 3 nor 5 | `"1"` |
| 2 | Neither divisible by 3 nor 5 | `"2"` |
| 3 | Divisible by 3 | `"Fizz"` |
| 4 | Neither divisible by 3 nor 5 | `"4"` |
| 5 | Divisible by 5 | `"Buzz"` |

Final Answer:

```python
["1", "2", "Fizz", "4", "Buzz"]
```
