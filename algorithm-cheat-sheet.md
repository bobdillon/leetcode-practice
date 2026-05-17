# Algorithm War Chest — Pattern Cheat Sheet

Read this before every session and before Tuesday.

---

## The Smells

**"I need to check if something exists in O(1)"**
→ Set. `num_set = set(nums)`. Lookup is `x in num_set`.
→ Also deduplicates automatically.

**"I need O(n) but would otherwise sort"**
→ Set instead of sort. Sorting is always O(n log n). Set build is O(n).

**"I'm comparing two elements and choosing WHICH one to advance"**
→ While loop, two pointers. `left = 0, right = len(arr) - 1`. Exit: `while left < right`.
→ For loops advance mechanically. While loops let you choose.

**"I'm walking two ends toward each other"**
→ Two pointers converging. While loop. Move the weaker/shorter/smaller pointer inward.

**"There's a carry or overflow that could chain"**
→ While loop with carry variable. `carry = total // 10`. Digit = `total % 10`.
→ Loop condition includes `or carry` to flush the last overflow.

**"I need to accumulate into buckets/rows/groups"**
→ List of n empty buckets. `buckets = [''] * n` or `[[] for _ in range(n)]`.
→ Walk the input, assign each element to the right bucket, combine at end.
→ `''.join(list_of_strings)` to concatenate.

**"Find best/longest/largest across a sequence that can break"**
→ Two variables: `current` and `best`. Reset `current` on break. `best = max(best, current)`.

**"Check all pairs"**
→ Nested for loops. `for i in range(n): for j in range(i+1, n)`.
→ This is O(n²). Fine if no time constraint. Ask about constraint first.

---

## Recurring Bugs to Avoid

**`i` in a for loop IS already the index.**
Stop using `list.index(i)`. That searches for a value, not a position.
`for i in range(len(arr))` → `arr[i]` is the element. `i` is the position.

**`len(arr)` counts from 1. Last index is `len(arr) - 1`.**
`range(len(arr))` goes 0 to n-1. Safe for indexing.
`range(len(arr) - 1)` stops one before the end — use when you access `arr[i+1]`.

**Off by one on streaks: start `current = 1`, not `0`.**
A single element is already a sequence of length 1.

**Read the time complexity constraint before writing a single line.**
O(n) stated → sort is off the table → think set or two pointers first.

---

## Skeletons

**Two pointers:**
```python
left, right = 0, len(arr) - 1
while left < right:
    # compute something with arr[left] and arr[right]
    if condition:
        left += 1
    else:
        right -= 1
```

**Carry loop:**
```python
carry = 0
i = 0
while i < len(l1) or i < len(l2) or carry:
    a = l1[i] if i < len(l1) else 0
    b = l2[i] if i < len(l2) else 0
    total = a + b + carry
    carry = total // 10
    result.append(total % 10)
    i += 1
```

**Set membership (O(n) consecutive/existence):**
```python
num_set = set(nums)
for n in num_set:
    if n - 1 not in num_set:  # start of sequence
        # count forward
```

**Best/current streak:**
```python
current, best = 1, 1
for i in range(len(arr) - 1):
    if arr[i+1] == arr[i] + 1:
        current += 1
        best = max(best, current)
    else:
        current = 1
```

**Row accumulation:**
```python
rows = [''] * nrows
current_row = 0
going_down = False
for char in s:
    rows[current_row] += char
    if current_row == 0 or current_row == nrows - 1:
        going_down = not going_down
    current_row += 1 if going_down else -1
return ''.join(rows)
```
