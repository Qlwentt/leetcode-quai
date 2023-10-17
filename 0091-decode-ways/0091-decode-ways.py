class Solution:
    def numDecodings(self, s: str) -> int:
        numMap = {str(num+1): letter for num, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
#         memo = {}
#         def backtrack(i):
#             if i > len(s):
#                 return 0
#             if i == len(s):
#                 return 1
#             if i in memo:
#                 return memo[i]
            
#             res = 0
#             # take only one num
#             nextNum = s[i]
#             if nextNum in numMap:
#                 res += backtrack(i+1)
            
#             # take two nums
#             nextNum = s[i:i+2]
#             if nextNum in numMap:
#                 res += backtrack(i+2)

#             memo[i] = res    
#             return res
                
#         return backtrack(0)
        def decodingDP():
            n = len(s)
            dp = [0]*(n+1)
            dp[n-1], dp[n] = 1 if s[-1] in numMap else 0 ,1
            
            i = n-2
            while i >= 0:
                print(s[i:i+2])
                dp[i] = (dp[i+1] if s[i] in numMap else 0) + (dp[i+2] if s[i:i+2] in numMap else 0)
                i -= 1
            print(dp)
            return dp[0]
        
        return decodingDP()
            
        