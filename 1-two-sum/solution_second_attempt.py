#hint - use a dict

# **Example 1:**
# ```
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# ```
#nums = [2,7,11,15]
#target=9
nums = [3,2,4]
target = 6
solution_indices = [0,1]
#nums = [0,1] - works

def summer(nums, target):
    seen = {} # key is number, value is its index
    # for i, num in enumerate(nums):
    #     number_i_need = target - num
    for i in range(len(nums)):
        num = nums[i]
        number_i_need = target - num
        if number_i_need in seen:
            return [seen[number_i_need], i]
        seen[num] = i
        print(seen)

ans = summer(nums, target)
print(ans)