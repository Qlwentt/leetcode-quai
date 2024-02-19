class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        memo = {}
        def dfs(r,c,prev):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                prev >= matrix[r][c]
               ):
                return 0
            if (r,c, prev) in memo:
                return memo[(r,c, prev)]
            cur = matrix[r][c]
            
            up = 1 + dfs(r-1, c, cur)
            down = 1 + dfs(r+1, c, cur)
            left = 1 + dfs(r, c-1, cur)
            right = 1 + dfs(r, c+1, cur)
            
            answer = max(up,down,left,right)
            memo[(r,c,prev)] = answer
            
            return answer
        longest = float('-inf')
        for r in range(ROWS):
            for c in range(COLS):
                longest = max(dfs(r,c, float('-inf')), longest)
        
        return longest