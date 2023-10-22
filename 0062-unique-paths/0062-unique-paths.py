class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    # memoization
        memo = {}
        def backtrack(row, col):
            if row >= m or col >= n:
                return 0
            if (row,col) == ((m-1), (n-1)):
                return 1
            if (row,col) in memo:
                return memo[(row,col)]

            left = backtrack(row, col+1)
            down = backtrack(row+1, col)

            memo[(row,col)] = left + down
            return memo[(row,col)]

        return backtrack(0,0)
    
    # dp
#         dp = [[0]*(n+1) for _ in range(m+1) ]
#         dp[m-1][n-1] = 1
        
#         for row in range(m-1, -1,-1):
#             for col in range(n-1, -1,-1):
#                 if (row, col) == (m-1, n-1):
#                     continue
#                 dp[row][col] = dp[row][col+1] + dp[row+1][col]
                
#         return dp[0][0]
        