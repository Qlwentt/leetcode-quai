class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
#         @cache
#         def dp(i):
#             if i == len(s):
#                 return True
            
#             for j in range(i, len(s)):
#                 cur_part = s[i:j+1]
#                 if cur_part in word_dict:
#                     if dp(j+1):
#                         return True
            
#             return False
#         return dp(0)
        dp = collections.defaultdict(lambda:False)
        n = len(s)
        dp[n] = True
        
        for i in range(n-1,-1,-1):
            for j in range(n-1,i-1, -1):
                cur_part = s[i:j+1]
                if cur_part in word_dict:
                    if dp[j+1]:
                        dp[i] = True
        return dp[0]
            
        