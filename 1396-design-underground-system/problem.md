# 1396. Design Underground System

**Difficulty:** Medium  
**Topic:** Hash Table, String, Design

## Problem Statement

An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the **average time** it takes to travel from one station to another.

Implement the `UndergroundSystem` class:

- `void checkIn(int id, string stationName, int t)`
  - A customer with a card ID equal to `id`, checks in at the station `stationName` at time `t`.
  - A customer can only be checked into one place at a time.
- `void checkOut(int id, string stationName, int t)`
  - A customer with a card ID equal to `id`, checks out from the station `stationName` at time `t`.
- `double getAverageTime(string startStation, string endStation)`
  - Returns the average time to travel between the `startStation` and the `endStation`.
  - The average time is computed from all the previous traveling from `startStation` to `endStation` that happened **directly** (without visiting other stations in between).
  - You may assume there will be at least one customer that has traveled from `startStation` to `endStation` before `getAverageTime` is called.

You may assume all calls to the `checkIn` and `checkOut` methods are consistent. If a customer checks in at time `t1` then checks out at time `t2`, then `t1 < t2`. All events happen in chronological order.

## Examples

**Example 1:**
```
Input:
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut",
 "getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],  [45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],
 [27,"Waterloo",20],[32,"Paradise",22],["Paradise","Waterloo"],["Leyton","Waterloo"],
 [10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output:
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]
```

## Constraints

- `1 <= id, t <= 10^6`
- `1 <= stationName.length, startStation.length, endStation.length <= 10`
- All strings consist of uppercase and lowercase English letters and digits.
- There will be at most `2 * 10^4` calls in total to `checkIn`, `checkOut`, and `getAverageTime`.
- Answers within `10^-5` of the actual value will be accepted.
