#nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]

# def consecutor(nums):
#     nums.sort()
#     print(nums)
#     length = 1
#     best = 1
#     for i in range(0,len(nums)-1):
#         if nums[i]==nums[i+1]-1:
#             length+=1
#             best = length
#         elif nums[i] == nums[i+1]:  # duplicate, just skip
#             pass
#         else:
#             length = 1
#     return best

# length = consecutor(nums)
# print(length)
#20 MIN, log n solution


# O(n) SET SOLUTION
def consecutor_on(nums):
    num_set = set(nums)       # O(n) — deduplicates and gives O(1) lookup
    best = 0

    for n in num_set:
        # Only start counting from the beginning of a sequence
        # A number is a sequence start if n-1 is NOT in the set
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            best = max(best, length)

    return best

print(consecutor_on([100,4,200,1,3,2]))   # 4
print(consecutor_on([0,3,7,2,5,8,4,6,0,1]))  # 9