class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        ROWS = len(matrix)
        COLS = len(matrix[0])
        def dfs(r,c, prev):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                matrix[r][c] <= prev
            ):
                return 0
            
            if (r,c) in memo:
                return memo[(r,c)]
            cur = matrix[r][c]
            up = dfs(r-1, c, cur) 
            down = dfs(r+1, c, cur)
            left = dfs(r, c-1, cur)
            right = dfs(r, c+1, cur)
            
            ans = max(up, down, left, right) + 1
            memo[(r,c)] = ans
            return ans
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, float('-inf'))
        
        return max(memo.values())
            
        