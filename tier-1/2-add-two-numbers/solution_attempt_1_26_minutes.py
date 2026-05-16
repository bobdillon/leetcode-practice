# Inputs 
l1 = [2,4,3]
l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# 10 min mark
# def add_two_numbers(l1,l2):
#     sum = []
#     for i in l1:
#         sum.append(i+l2[l1.index(i)])
 
#     for i in sum:
#         if i>=10:
#             sum[i]=sum[i][1]
#             sum[i+1]+=1
#     return sum[::-1]

# ans = add_two_numbers(l1,l2)
# print(ans)
def add_two_numbers(l1,l2):
    carry = 0
    i = 0
    result = []
    # keep looping as long as there's either more 
    # digits to process OR a leftover carry to flush.
    while i < len(l1) or i < len(l2) or carry:
        a = l1[i] if i < len(l1) else 0
        b = l2[i] if i < len(l2) else 0
        total = a + b + carry
        carry = total // 10
        result.append(total % 10)
        i += 1
    return result
   

ans = add_two_numbers(l1,l2)
print(ans)