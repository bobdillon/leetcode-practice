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
