# 1146. Snapshot Array

**Difficulty:** Medium  
**Topic:** Array, Hash Table, Binary Search, Design

## Problem Statement

Implement a SnapshotArray that supports the following interface:

- `SnapshotArray(int length)` Initializes an array-like data structure with the given length. **Initially, each element equals 0**.
- `void set(int index, int val)` Sets the element at the given `index` to be equal to `val`.
- `int snap()` Takes a snapshot of the array and returns the `snap_id`: the total number of times we called `snap()` minus `1`.
- `int get(int index, int snap_id)` Returns the value at the given `index`, at the time we took the snapshot with the given `snap_id`.

## Examples

**Example 1:**
```
Input:
["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]

Output:
[null,null,0,null,5]

Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // [0, 0, 0]
snapshotArr.set(0, 5);  // [5, 0, 0]
snapshotArr.snap();     // snap_id = 0, returns 0
snapshotArr.set(0, 6);  // [6, 0, 0]
snapshotArr.get(0, 0);  // returns 5 (value at index 0 when snap_id=0 was taken)
```

## Constraints

- `1 <= length <= 5 * 10^4`
- `0 <= index < length`
- `0 <= val <= 10^9`
- `0 <= snap_id <` (the total number of times we call `snap()`)
- At most `5 * 10^4` calls will be made to `set`, `snap`, and `get`.

