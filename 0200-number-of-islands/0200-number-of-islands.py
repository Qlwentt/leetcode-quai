class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        def dfs(row,col):
            if (row not in range(ROWS) or
                col not in range(COLS) or
                (row,col) in visited or
                grid[row][col] == "0"):
                return 0
            
            visited.add((row,col))
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
            
            return 1
        answer = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    answer += dfs(row,col)
        return answer
            