# 359. Logger Rate Limiter — Post-Solve Notes

## Approach & Design Choices


## Tradeoffs


## Edge Cases Considered


## Time & Space Complexity


## Likely Follow-up Extensions


## What I'd Do Differently


## Lessons Learned (Personal Reminders)

**1. Clarify the problem immediately — especially the input format.**
Before writing a single line, confirm what the function signature looks like and what's actually being passed in. On LeetCode the stub is pre-written; in an interview the interviewer hands it to you. Either way, you should never have to guess. If the directions are unclear, ask within the first 2 minutes.

**2. Store the minimum data needed to solve the exact problem. No more.**
The instinct to track all timestamps, all logs, future-proof for a database — stop. That exceeds scope and adds complexity that introduces bugs. Ask: *"what is the bare minimum state I need to answer this specific question?"* Then store only that. Here it was one integer per message — the last printed timestamp. Nothing else.

**3. Do not exceed scope. Solve atomically.**
What they asked for is a boolean per call. Not a log history. Not a database-ready structure. Solve the problem in front of you, not the imagined problem downstream. Future-proofing in an interview is a liability, not a strength.

**4. Before putting your pencil down, audit every return path.**
Trace through at least one full example manually and confirm:
- Every branch returns the right type
- No branch falls through and returns `None` by accident
- The True/False logic matches the problem's definition of "should print"

Do this before saying you're done, not after.
