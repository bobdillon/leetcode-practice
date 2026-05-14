# **Example 1:**
# ```
# Input: 
intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: 
ans = [[1,6],[8,10],[15,18]]
"""Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6]."""

# **Example 2:**
#Input: 
intervals2 = [[1,4],[4,5]]
#Output:
ans2 = [[1,5]]
"""Explanation: Intervals [1,4] and [4,5] are considered overlapping."""


def interval_overlap(intervals):
    map = {}
    ans = []
    for i in intervals:
        position = intervals.index(i)
        #print(position)
        min = i[0]
        max = i[1]
        #print(min,max)
        # next_min = next_position[0]
        # next_max = next_position[1]
        # print(next_min, next_max)


        map[position] = [min, max]
    for i in range(len(map)-1):
        print(map[i])
        #if map[i][0]<=map[i+1][0] and map[i][1]>=map[i+1][0]:
        if map[i][1]>=map[i+1][0]:
            ans.append([map[i][0], map[i+1][1]])
        else:
            ans.append(map[i])
        #print(i[0])
        #if i[0]<=i[1] and 

    
    #print(map)
    #ans = 'hold'
    return ans

ans = interval_overlap(intervals)
print(ans)

# --- fixed version ---
def interval_overlap_fixed(intervals):
    intervals.sort(key=lambda x: x[0])
    map = {}
    ans = []
    for i in intervals:
        position = intervals.index(i)
        map[position] = [i[0], i[1]]
    for i in range(len(map)-1):
        if map[i][1] >= map[i+1][0]:
            map[i+1] = [map[i][0], max(map[i][1], map[i+1][1])]  # merge into next slot, carry forward
        else:
            ans.append(map[i])
    ans.append(map[len(map)-1])  # always add last interval
    return ans

print(interval_overlap_fixed(intervals))

# --- fixed version 2: no map, with sort ---
def interval_overlap_v2(intervals):
    # sort by start value of each interval
    intervals.sort()  # sorts by first element by default, no lambda needed
    """ holy shit, default sort can handle elements with multiple things in them !"""

    ans = [intervals[0]]  # seed the answer with the first interval

    for i in range(1, len(intervals)):
        current_start = intervals[i][0]
        current_end = intervals[i][1]
        last_end = ans[-1][1]  # end of the last interval we committed to ans

        if current_start <= last_end:
            # overlap — extend the last interval in ans if needed
            ans[-1][1] = max(last_end, current_end)
        else:
            # no overlap — just add it
            ans.append(intervals[i])

    return ans

print(interval_overlap_v2(intervals))