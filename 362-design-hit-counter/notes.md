# 362. Design Hit Counter — Post-Solve Notes

## My Notes (raw, first attempt)
keep it very tightly knit to the directions

tradeoff: if future method needs to check number of hits at a timestamp, this class breaks

indent of class functions needs to be same as init

think very carefully of whats being asked, 
wasted time making a more complex data structure than needed

know popleft, pop, extend, append, deque, orderdict

---

## Approach & Design Choices
Used a deque from collections. Each call to hit() appends the timestamp integer to the deque.
Each call to getHits() trims the left side of the deque (popleft) while the oldest entry is
more than 300 seconds ago (entry <= timestamp - 300), then returns len(deque).
The elegance: every append represents one hit. No linking timestamps to counts needed.
The timestamp IS the data.

## Tradeoffs
Simple append-per-hit approach breaks if a future method needs hits-per-timestamp breakdown.
In that case you'd need (timestamp, count) tuples or a dict. But for this problem, overkill.
Space: O(n) where n = total hits in the last 300 seconds.
Time: O(1) amortized for both hit() and getHits() — each timestamp is added and removed at most once.

## Edge Cases Considered
- Multiple hits at the same timestamp — handled correctly, just append same timestamp multiple times
- getHits called with no hits in last 300s — while loop clears everything, returns 0
- "Last 300 seconds" means timestamp - 300, NOT last 300 hits (important wording distinction)

## Time & Space Complexity
hit(): O(1)
getHits(): O(n) worst case for the cleanup loop, but O(1) amortized
Space: O(n) — deque holds at most all hits in the 300s window

## Pattern
Sliding Window over time — deque with left-trim on stale entries. Same mental model as
sliding window on arrays but the window is defined by time delta instead of index delta.

## Likely Follow-up Extensions
- What if you need hits per specific timestamp? → store (timestamp, count) tuples or a dict
- What if hits can arrive out of order? → current solution breaks, would need a sorted structure
- Scale to millions of hits/sec? → bucketing by second (array of 300 buckets) is more memory efficient

## What I'd Do Differently
- Don't use extend() when you mean append() — extend adds each element of a list separately
- Class methods must be at the same indentation level as __init__, not nested inside it
- Don't pre-populate the deque with range(1,300) — start empty, append real data only
- State assumptions out loud: "timestamps are always increasing integers in seconds"
- Say "last 300 seconds" not "last 300 hits" — precision matters in interviews