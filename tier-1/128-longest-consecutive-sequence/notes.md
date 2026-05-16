# 128. Longest Consecutive Sequence — Post-Solve Notes

## Attempt 1 — May 15, 2026 | ~30 min | 1 hint (set) + shown O(n) solution

### Assessment: L4 (would not pass as-is — violated explicit O(n) constraint)
All correct logic and instincts. Wrong data structure. Would have been a pass
if the O(n) constraint wasn't stated, or if armed with the set pattern.

---

## What Happened

**First attempt (~20 min):** Sorted + for loop with current/best streak tracking.
- Correct approach conceptually
- Correctly handled duplicates with `elif nums[i] == nums[i+1]: pass`
- Correctly used `best = 1` (not 0) to handle no-consecutive-pairs case
- **Fatal flaw:** `nums.sort()` is O(n log n) — violates explicit constraint

**Hint given:** "What data structure gives O(1) lookup?" → set

**Couldn't arrive at O(n) independently** — shown the set solution.

---

## The O(n) Set Solution

```python
def consecutor_on(nums):
    num_set = set(nums)       # O(n), deduplicates, O(1) lookup
    best = 0
    for n in num_set:
        if n - 1 not in num_set:   # only start from sequence beginnings
            length = 1
            while n + length in num_set:
                length += 1
            best = max(best, length)
    return best
```

**The key insight:** Only start counting from sequence beginnings.
- If `n-1` is in the set, `n` is in the middle of a sequence — skip it
- If `n-1` is NOT in the set, `n` is the start — count forward with while loop
- Each number is visited exactly once total → O(n) despite nested while loop

---

## The Core Pattern to Remember
**"O(n) + need to check membership" = set**

Any time a problem says O(n) and you'd otherwise sort, ask:
*Can a set replace the sort?*

- `set(nums)` is O(n) to build
- `x in num_set` is O(1) to check
- Duplicates are handled automatically

---

## Edge Cases
- Duplicates: set deduplicates automatically — no need for elif skip logic
- Single element: `n-1 not in set` → while loop never runs → length=1 → correct
- Empty array: `best=0`, loop never runs → returns 0 → correct

---

## Time & Space Complexity
- O(n log n) sort solution: fails the constraint
- O(n) set solution:
  - Time: O(n) — each element visited once
  - Space: O(n) — the set

---

## What to Work On
- **Read the time constraint before choosing your algorithm.** O(n) stated
  explicitly = sort is off the table. Ask "what gets me O(1) lookup?" immediately.
- **Set pattern:** When you need O(n) and membership checking, reach for set first.
- **Strong instincts, wrong tool:** The current/best streak logic, duplicate 
  handling, and sequence-start detection were all correct. Just needed set instead of sort.
