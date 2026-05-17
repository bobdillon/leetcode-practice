height = [1,8,6,2,5,4,8,3,7]

# ATTEMPT 1 — wrong approach (tracking running max, not all pairs)
# def bucket(height):
#     champion_length = 1
#     champion_width = 1
#     for i in range(len(height)-1):
#         if champion_length<=height[i+1]:
#             champion_length = height[i+1]
#             #champion_width = height.index(i+1) - height.index(champion_length)
#         # elif champion_length==height[i+1]:
#         #     champion_width
#     return champion_length#*champion_width


# O(n²) BRUTE FORCE — correct, but slow
def bucket_n2(height):
    best = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = min(height[i], height[j]) * (j - i)
            best = max(best, area)
    return best

# O(n) TWO POINTER SOLUTION
def bucket(height):
    left = 0
    right = len(height) - 1
    best = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        best = max(best, area)
        if height[left] < height[right]:
            left += 1   # shorter bar on left, move it inward
        else:
            right -= 1  # shorter bar on right, move it inward
    return best

print(bucket(height))  # 49

