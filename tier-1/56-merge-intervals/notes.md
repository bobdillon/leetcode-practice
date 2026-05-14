# 56. Merge Intervals — Post-Solve Notes

## Approach & Design Choices
First attempt (~25 min): built a hash map where keys were positions and values were [start, end] pairs, then looped over the map comparing adjacent intervals. Overlap condition was initially wrong (`end < next_end` instead of `end >= next_start`). Core merge logic was close but appending immediately to `ans` caused duplicate/stale entries when 3+ intervals chain together.

Fixed map version: on overlap, wrote merged result back into `map[i+1]` instead of appending, so the next iteration sees the already-merged interval. Added `ans.append(map[len(map)-1])` after the loop to capture the last interval.

Clean version (v2 — the right way): sort input first with `intervals.sort()`, seed `ans` with the first interval, then loop from index 1. On each step compare `current_start` against `ans[-1][1]` (last committed end). If overlap, extend `ans[-1][1]` in place. Otherwise append. No map needed.

Missed sorting entirely in the attempt — problem does NOT guarantee sorted input. Should always ask/state this assumption before coding.

## Tradeoffs
Map version: unnecessary extra O(n) space for a structure that just duplicates the input. Adds complexity with no benefit.
V2: `ans` list does double duty as both the working state and the final answer — cleaner and still O(n) space.

## Edge Cases Considered
- Input not sorted — must sort first or logic breaks entirely
- 3+ intervals that all overlap and need to chain-merge (e.g. `[[1,3],[2,5],[4,7]]` → `[[1,7]]`)
- Adjacent intervals that touch but don't overlap (e.g. `[1,4],[4,5]` — the `>=` handles this)
- Single interval input — v2 handles this because `ans` is seeded with `intervals[0]` and the loop simply doesn't run

## Time & Space Complexity
O(n log n) time — dominated by the sort step
O(n) space — output list in worst case is same size as input (no merges)

## Pattern
Sort Then Scan — sort by start value, then one linear pass with a running "current window" in `ans`

## Likely Follow-up Extensions
- What if input intervals are given as objects, not lists? (need to sort by attribute)
- What if you need to find the *gaps* between merged intervals instead of the merged ones?
- Insert a new interval into an already sorted, merged list (LeetCode 57 — natural follow-up)

## What I'd Do Differently
1. Ask upfront: "is input guaranteed sorted?" — if not, sort first, always
2. Skip the map entirely — when you find yourself building a dict that just copies the input, stop and ask if you actually need it
3. Seed `ans` with the first element and loop from index 1 — this pattern avoids all off-by-one issues with the last element
4. Recognize this as Sort Then Scan pattern earlier — the moment you see "merge" + "intervals/ranges", think sort first
