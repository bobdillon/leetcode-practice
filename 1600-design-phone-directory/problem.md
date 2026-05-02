# 1600. Design Phone Directory

**Difficulty:** Medium  
**Topic:** Design, Hash Table, Linked List, Queue

## Problem Statement

Design a phone directory that initially has `maxNumbers` empty slots that can store numbers. The directory should store numbers, as well as support querying available numbers (to assign) and releasing previously assigned numbers.

Implement the `PhoneDirectory` class:

- `PhoneDirectory(int maxNumbers)` Initializes the phone directory with the number of available slots `maxNumbers`.
- `int get()` Provides a number that is not assigned to anyone. Returns `-1` if no number is available.
- `bool check(int number)` Returns `true` if the slot `number` is available, `false` otherwise.
- `void release(int number)` Recycles or releases a number back to the pool.

## Examples

**Example 1:**
```
Input:
["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
[[3], [], [], [2], [], [1], [2], [2]]

Output:
[null, 0, 1, true, 2, false, null, true]

Explanation:
PhoneDirectory phoneDirectory = new PhoneDirectory(3);
phoneDirectory.get();      // return 0, slot 0 is assigned
phoneDirectory.get();      // return 1, slot 1 is assigned
phoneDirectory.check(2);   // return true, slot 2 is still available
phoneDirectory.get();      // return 2, slot 2 is assigned
phoneDirectory.check(1);   // return false, slot 1 is assigned
phoneDirectory.release(2); // release slot 2 back to pool
phoneDirectory.check(2);   // return true, slot 2 is available again
```

## Constraints

- `1 <= maxNumbers <= 10^4`
- `0 <= number < maxNumbers`
- At most `2 * 10^4` calls will be made to `get`, `check`, and `release`.
