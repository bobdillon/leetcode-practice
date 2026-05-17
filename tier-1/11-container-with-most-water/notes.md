# 11. Container With Most Water - Post-Solve Notes

## Attempt 1 - May 16, 2026 | ~45 min | shown O(n) solution

### Assessment: L4 (O(n^2) brute force arrived at independently, O(n) not reached)

---

## Solutions

**O(n^2) brute force - arrived at independently:**
```python
def bucket(height):
    best = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = min(height[i], height[j]) * (j - i)
            best = max(best, area)
    return best
```

**O(n) two pointer - shown:**
```python
def bucket(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        best = max(best, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
```

---

## When to Use a While Loop vs For Loop
**The tell: Am I choosing between moving left or right based on a comparison?**
-> While loop, two pointers.

A for loop advances mechanically - one iterator, one direction.
A while loop lets you conditionally advance EITHER pointer based on logic.

Two pointer smell: two ends of an array converging toward each other.
Exit condition is always: while left < right

---

## Why Move the Shorter Bar Inward?
Width shrinks by 1 no matter which pointer you move.
So the only way to improve area is to find a taller bar.
The taller bar is already doing its job - moving it inward can only hurt.
Move the shorter one and hope the next bar is taller.

---

## Recurring Bug - Read This Before Every Attempt
i in a for loop IS the index. Stop calling list.index(i) to find it.
for i in range(len(height)) -> i is already the position. Just use i.
height.index(x) searches for a VALUE - that is almost never what you want.
