class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        memo = {}
        
        def dfs(r,c, prev):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                matrix[r][c] <= prev
               ):
                return 0
            
            if (r,c) in memo:
                return memo[(r,c)]
            cur = matrix[r][c]
            up = 1 + dfs(r-1, c, cur)
            down = 1 + dfs(r+1, c, cur)
            left = 1 + dfs(r, c-1, cur)
            right = 1 + dfs(r, c+1, cur)
            
            answer = max(up, down, left, right)
            memo[(r,c)] = answer
            return answer
        maxLen = 1
        for r in range(ROWS):
            for c in range(COLS):
                maxLen = max(maxLen, dfs(r,c, float('-inf')))
        return maxLen
# Time: O(M*N)
# Space: O(M*N)