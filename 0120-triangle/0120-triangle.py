class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
#         @cache
#         def dp(i,j):
#             if i == len(triangle):
#                 return 0
            
#             left = triangle[i][j] + dp(i+1,j)
#             right = float('inf')
#             if j + 1 in range(len(triangle[i])):
#                 right = triangle[i][j+1] + dp(i+1,j+1)
            
#             return min(left,right)
#         return dp(0,0)

        dp = collections.defaultdict(lambda: collections.defaultdict(int))
    
        for i in range(len(triangle)-1,-1,-1):
            for j in range(len(triangle[i])-1,-1,-1):
                left = triangle[i][j] + dp[i+1][j]
                right = float('inf')
                if j + 1 in range(len(triangle[i])):
                    right = triangle[i][j+1] + dp[i+1][j+1]
                dp[i][j] = min(left, right)
        return dp[0][0]
            
            