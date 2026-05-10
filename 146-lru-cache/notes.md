# 146. LRU Cache — Post-Solve Notes

## Approach & Design Choices


## Tradeoffs


## Edge Cases Considered
since its always integers and a value cant be none, 
is not none is ok 

## Time & Space Complexity


## Likely Follow-up Extensions


## What I'd Do Differently


---

## Attempt 2 — Key Reminders

**OrderedDict is the right tool here.** It maintains insertion order and gives you O(1) get, put, and reorder.

**Critical methods to remember:**
- `move_to_end(key)` — moves a key to the most recently used position (end). Use this in `get` AND `put`.
- `popitem(last=False)` — removes the least recently used item (front). Use this to evict when over capacity.

**The bug to never repeat:**
`get` is an access. Every access updates recency — not just `put`. If `get` doesn't call `move_to_end`, recently-read keys can be evicted incorrectly. Always ask: *does every operation that touches a key also update its recency?*

**Google L5 self-assessment:**
- With the get bug: strong L4. Logic and explanation were excellent, but missing recency on get is a core miss.
- Without the bug (self-caught): clean L5. 15 min on a Medium with full verbal explanation and correct code is the bar.


know - 
ordereddict, 
move_to_end(key), 
popitem(last=bool)