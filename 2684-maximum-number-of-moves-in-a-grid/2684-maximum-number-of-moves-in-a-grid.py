class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        cache = {}
        def dfs(r,c, prev):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] <= prev
            ):
                return 0
            if (r,c,prev) in cache:
                return cache[(r,c,prev)]
            
            up_right = dfs(r-1,c+1, grid[r][c])
            right = dfs(r,c+1, grid[r][c])
            down_right = dfs(r+1,c+1, grid[r][c])
            
            ans = max(up_right, right, down_right) + 1
            cache[(r,c,prev)] = ans
            return ans
        answer = 0
        for r in range(ROWS): 
            answer = max(answer, dfs(r,0, float('-inf'))) 
                
        return answer - 1
        