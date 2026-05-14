# 3. Longest Substring Without Repeating Characters — Post-Solve Notes

## Approach & Design Choices
Used a hash map (dict) to store each character as a key and its index in the string as the value.
Looped over the string by index. On each iteration, checked if the current character was already in the map.
If it was, computed the window length as `i - seen[s[i]]` and took the max with the current answer.
Then updated `seen[s[i]] = i` to keep the map current.

Got to this point (~40 min) independently. The map structure and storing indices was self-derived.

## Where I Got Stuck
Could not figure out the `start` variable on my own. The issue was that `ans` only updated when a duplicate was found — strings with no repeats (e.g. "abcd") would incorrectly return 1.
The fix required a `start` pointer that tracks the beginning of the current valid window, updated to `seen[s[i]] + 1` on a duplicate. Then `ans = max(ans, i - start + 1)` runs every iteration, not just on duplicates.

## Tradeoffs
Hash map trades O(n) space for O(n) time vs a brute force O(n^2) nested loop approach.

## Edge Cases Considered
- String of all same characters e.g. "bbbbb" → answer is 1
- String with no repeats e.g. "abcd" → answer is full length (this is where the bug was)

## Time & Space Complexity
O(n) time — single pass through the string
O(n) space — hash map stores at most n characters

## Pattern
Sliding Window — this is a classic sliding window problem. The `start` pointer is the left edge of the window, `i` is the right edge.

## Likely Follow-up Extensions
- What if you need to return the actual substring, not just the length?
- What if characters have a max frequency > 1 (e.g. at most k repeats allowed)?

## What I'd Do Differently
Recognize the sliding window pattern earlier — the moment you have a "current window" with a left and right boundary, think sliding window.
