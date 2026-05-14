#feed back attempt 1- 
Verbal explanation: 4.5/5 — that was a genuinely strong walkthrough. Clear entity identification, justified every design decision, explained the data flow end to end. That's exactly what FDE interviewers want.

Code: 3.5/5 — structure is right, two bugs:

self.lot(size) — parentheses instead of brackets. Should be self.lot[size]

Payment calculation in exit — datetime.timedelta() doesn't work that way. You already have datetime objects so just subtract them directly:

Parking.__init__ takes vehicle — it shouldn't. Same issue as before: the lot exists independently of any vehicle. Just def __init__(self):.

truck = Vehicle() — indented wrong (stray space) and missing the argument: Vehicle('truck')

Fix those and the solution is complete and correct. The verbal was the stronger part today — which is actually what matters most for Monday.



# Parking Lot OOP Design — Post-Solve Notes

## Approach & Design Choices


## Tradeoffs


## Edge Cases Considered


## Time & Space Complexity


## Likely Follow-up Extensions


## What I'd Do Differently

---

## Attempt 2 — 33 minutes

**Google L5 assessment: solid L4, borderline L5**
Design instincts are strong. Entities well-chosen (Vehicle, Ticket, ParkingLot). Mutable lot tracker is the right approach. Explanation was clear, methodical, and justified every decision. Bugs were implementation-level, not conceptual.

**Bugs found:**

1. **`allocate_spot` — wrong slice index**
   `self.lot[vehicle.size][:-1]` returns a list, not a single element. Should be `[-1]` to get the last spot number.

2. **`report_capacity` — wrong iteration**
   `for i in self.lot` gives you the string key (e.g. `'large'`). Then `i[0]` is `'l'` and `i[1]` is `'a'` — characters of the string, not dict elements.
   Fix: `print(f'There are {len(self.lot[i])} {i} spots left')`

3. **`calculate_payment` — timedelta math**
   `datetime.now() - ticket.timestamp` returns a `timedelta` object. You can't `// 60` it directly.
   Fix: `(current - ticket.timestamp).seconds // 3600 * 5` for hourly billing, or `.seconds // 60 * 5` for per-minute.

4. **`Ticket` doesn't store spot number (commented out)**
   In production this matters — the garage needs to know which spot to free without depending on the vehicle object still being present. Consider keeping it in.

**What went well:**
- OOP decomposition was clean and justified
- Verbal explanation was the strongest part — end-to-end, no gaps
- Mutable lot tracker with pop/append is exactly right

**Reminder:**
After writing any indexing or iteration, trace through one example manually before moving on. `[-1]` vs `[:-1]` and `for i in dict` vs `for k, v in dict.items()` are easy to mix up under pressure.
