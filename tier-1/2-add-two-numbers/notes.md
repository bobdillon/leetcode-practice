# 2. Add Two Numbers — Post-Solve Notes

## Attempt 1 — May 15, 2026 | ~26 min | 1 hint

### Assessment: L4 / Borderline L5
Correct final solution. Got there with one hint. Strong conceptual instincts,
but the first implementation had structural errors that needed to be talked through.

---

## What Happened

**First attempt (~10 min):** Two-pass approach — element-wise sum first, then a
second loop to fix carries. Good instinct to decompose the problem, but flawed:
- Used `l1.index(i)` instead of index-based iteration (breaks on duplicate values)
- Tried to use the value `i` as an index (`sum[i]`) instead of a position counter
- Two-pass carry-fixing can't handle carry chains without a nested while loop
- Would have needed `[::-1]` unnecessarily (output is also reversed)

**Hint given:** One-pass while loop with carry variable and index pointer.

**After hint (~16 min):** Rebuilt correctly. Got all the pieces right:
- `while i < len(l1) or i < len(l2) or carry` — correct termination condition
- `a = l1[i] if i < len(l1) else 0` — correct length-mismatch handling
- `carry = total // 10`, `result.append(total % 10)` — correct carry math

---

## Key Concepts

**The carry variable pattern:**
```python
carry = 0
i = 0
result = []
while i < len(l1) or i < len(l2) or carry:
    a = l1[i] if i < len(l1) else 0
    b = l2[i] if i < len(l2) else 0
    total = a + b + carry
    carry = total // 10       # 1 if overflow, 0 if not
    result.append(total % 10) # the digit to keep
    i += 1
return result
```

**Why `or carry` in the while condition:**
Handles the edge case where the final addition overflows (e.g. 999 + 1 = 1000).
Both lists are exhausted but there's still a carry=1 that needs to become a new digit.

**`// 10` vs `% 10`:**
- `total // 10` → carry (0 or 1)
- `total % 10` → digit to append
Easy to swap these — double-check when writing under pressure.

**No reversal needed:**
Input AND output are both in reverse digit order. The while loop naturally
builds the result in the correct output order.

---

## Edge Cases
- Lists of different lengths → handled by `else 0` fallback
- Final carry overflow (999 + 1 = 1000) → handled by `or carry` in while condition
- Carry chain (999 + 999) → handled naturally, carry flushes each iteration

---

## Time & Space Complexity
- Time: O(max(m, n)) — one pass through the longer list
- Space: O(max(m, n) + 1) — result list

---

## Interview Communication
- **Talk the whole time.** Even when stuck, narrate: "I'm thinking about whether I need to handle unequal lengths here..." 
  Silence reads as "this person is lost." Narration reads as "this person thinks out loud like a senior engineer."
- If you catch your own bug verbally before fixing it, that's actually a positive signal — shows self-awareness.
- If you need a hint, frame it: "I think I need a while loop here — does that direction make sense?" 
  Asking targeted questions > sitting in silence.

## What to Work On
- **Index vs value confusion:** When iterating, default to `for i in range(len(...))` 
  or a manual index counter. `list.index(val)` is almost never what you want in 
  these problems — it finds the *first* occurrence, not the current position.
- **Boundary conditions before indexing:** Before reaching for `list[i]`, ask 
  "what if i is out of bounds?" The ternary `x[i] if i < len(x) else 0` is the 
  clean pattern here.
- **Sniffed out the right structure:** Correctly predicted "pointer + while loop" 
  before being told the solution. That instinct is real — trust it earlier and 
  try to build the while loop from scratch next time before falling back to for loops.
