class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        
        def dfs(r,c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r,c) in visited or
                grid[r][c]== "0"):
                return False
            
            visited.add((r,c))
            
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r, c-1)
            dfs(r, c+1)
            return 1
        answer = 0
        for r in range(ROWS):
            for c in range(COLS):
                answer += dfs(r,c)
        
        return answer
                