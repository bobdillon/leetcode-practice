## Problem Statement

"""Given a string `s`, find the length of the **longest substring** without 
repeating characters."""


# Ex 1
s = "abcabcbb"
ans=3

# Ex 2
s = "abcabcbb"
ans=3

# Ex 3
s = "pwwkew"
ans = 3

# p 2
# w 1
# w 2
# k 3
# e 1
# w 2

def substring_finder(s):
    seen = {}
    ans=1
    for i in range(len(s)):
        # #for j in range(len(s)):
        if s[i] in seen:
            ans = max(ans, i - seen[s[i]])
        #     seen[s[i]] = i
        # else:    
        #     seen[s[i]]= i
        #     print(seen)
        else:
            pass

        seen[s[i]]= i
        print(seen)
        
        # if s[i] != s[i+1]:
        #     ans+=1
        # else:
        #     ans=1
        # seen[s[i]]= ans
        # print(seen)
    #ans = 
    return ans

#given full solution by claude
def substring_finder(s):
    seen = {}
    ans = 1
    start = 0                          # start of current window
    for i in range(len(s)):
        if s[i] in seen:
            start = seen[s[i]] + 1     # jump start past the duplicate
        seen[s[i]] = i
        ans = max(ans, i - start + 1)  # always update ans
    return ans

ans = substring_finder(s)
print(ans)