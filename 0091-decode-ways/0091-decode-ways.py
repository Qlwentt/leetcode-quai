class Solution:
    def numDecodings(self, s: str) -> int:
#         @cache
#         def backtrack(i):
#             if i >= len(s):
#                 return 1
#             count  = 0
#             for j in range(i,len(s)):
#                 substring = s[i:j+1]
#                 if substring[0] != "0" and int(substring) in range(1,27):
#                     count += backtrack(j+1)
            
#             return count
            
#         return backtrack(0)
#         @cache
#         def backtrack(i):
#             if i == len(s):
#                 return 1
            
#             # take one
#             next_num = s[i]
#             count = 0
#             if int(next_num) in range(1,27) and next_num[0] != "0":
#                 count += backtrack(i+1)
                
#             if i+1 in range(len(s)):
#                 next_num = s[i] + s[i+1]
#                 if int(next_num) in range(1,27) and next_num[0] != "0":
#                     count += backtrack(i+2)
            
#             return count
#         return backtrack(0)
        n = len(s)
        dp = collections.defaultdict(int)
        dp[n] = 1
        
        for i in range(n-1,-1,-1):
            next_num = s[i]
            if int(next_num) in range(1,27) and next_num[0] != "0":
                dp[i] += dp[i+1]
            if i + 1 in range(n):
                next_num = s[i] + s[i+1]
                if int(next_num) in range(1,27) and next_num[0] != "0":
                    dp[i] += dp[i+2]
        
        return dp[0]
                
                
        
             
        