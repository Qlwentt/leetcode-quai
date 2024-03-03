class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        memo = {}
        def dfs(prev, r,c):
            
            
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                prev >= matrix[r][c]
            ):
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            cur = matrix[r][c]
            up = dfs(cur, r - 1, c) 
            down = dfs(cur, r+1, c)
            left = dfs(cur, r, c-1)
            right = dfs(cur, r, c+ 1)
            
            answer = max(up, down, left, right) + 1
            memo[(r,c)] = answer
            return answer
        longestPath = 0
        for r in range(ROWS):
            for c in range(COLS):
                longestPath = max(dfs(float('-inf'), r,c), longestPath)
        
        return longestPath