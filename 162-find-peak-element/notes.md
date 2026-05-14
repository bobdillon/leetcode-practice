# 162. Find Peak Element — Post-Solve Notes

## Approach & Design Choices


## Tradeoffs


## Edge Cases Considered


## Time & Space Complexity


## Likely Follow-up Extensions


## What I'd Do Differently
---

## Attempt 1 — 30 minutes (2 hints used)

**Final solution: correct and clean.** Textbook binary search, right pointer movement, right convergence, right return.

**Revised Google L5 assessment: Strong L3, weak L4.**
Two hints in 30 minutes on a Medium drops the rating. At L5, the expectation is recognizing binary search from the O(log n) constraint immediately and implementing it without guidance. The concept had to be explained, which in a real interview means the interviewer carried part of the problem.

---

**Where I struggled:**

1. **Didn't read the constraints** — missed the O(log n) requirement entirely and submitted an O(n) solution thinking it was done. Always read constraints before coding.

2. **Didn't know binary search cold** — needed the slope logic (compare mid to mid+1 to decide which half) explained from scratch. This is a must-know pattern. Drill it until it's automatic.

3. **Slice approach detour** — tried to shrink the array instead of using pointers, which loses index information. Pointers are always the right move for binary search in Python.

4. **index/value confusion** — `mid = nums[len//2]` got the value instead of the index, then tried to use it as an index. Always name clearly: `mid_idx` vs `mid_val` if it helps, or just remember `mid` is always an index.

5. **Wrong return** — tried `nums.index(mid)` at the end instead of just `return left`. When pointers converge, `left` IS the answer — no lookup needed.

---

**Patterns to internalize:**

- **O(log n) in the constraints = binary search.** No exceptions.
- **Binary search skeleton:**
  ```python
  left, right = 0, len(nums) - 1
  while left < right:
      mid = (left + right) // 2
      if condition:
          left = mid + 1
      else:
          right = mid
  return left
  ```
- **Never modify the array in binary search.** Use pointers.
- **`return left` when converged** — no value lookup needed.