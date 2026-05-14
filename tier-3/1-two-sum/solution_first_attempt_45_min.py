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

def two_sum(nums, target):
    # if len(nums) == 2:
    #     return solution_indices
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            print (i, j)
            sum = nums[i]+nums[j]
            print(sum)
            if sum==target:
                #solution_indices = [i,j]
                #return solution_indices
                return [i,j]


        
if len(nums) == 2:
    ans = [0,1]
ans = two_sum(nums, target)
print(ans)
