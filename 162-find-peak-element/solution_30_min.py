# nums = [1,2,3,1]
# ans = 2

nums = [1,2,1,3,5,6,4]
ans = 5



# def find_peak_element_index(nums):
#     ans = nums.index(max(nums))
#     return ans

# ans = find_peak_element_index(nums)
# print(ans)


# def find_peak_element_index(nums):
#     while len(nums)>1:
#         mid = len(nums)//2
#         print(mid)
#         if nums[mid]<nums[mid+1]:
#             nums = nums[mid:]
#         else:
#             nums = nums[:mid]
#     return nums[0]

# ans = find_peak_element_index(nums)
# print(ans)

def find_peak_element_index(nums):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left + right) //2
        if nums[mid]<nums[mid+1]:
            left=mid+1
        else:
            right=mid
    return left

ans = find_peak_element_index(nums)
print(ans)