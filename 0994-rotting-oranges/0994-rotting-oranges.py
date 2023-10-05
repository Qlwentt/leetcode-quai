from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque([])
        visited = set()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                if grid[r][c] == 1:
                    fresh += 1
        
        time = 0
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        while q:
            r, c, minute = q.popleft()
            
            time = max(minute, time)
            for dr, dc in directions:
                newRow = dr + r
                newCol = dc + c
                if (newRow in range(ROWS) and 
                    newCol in range(COLS) and
                    grid[newRow][newCol] == 1 and
                    (newRow,newCol) not in visited
                   ):
                    q.append((newRow, newCol, minute +1))
                    visited.add((newRow,newCol))
                    
        return time if len(visited) == fresh else -1
            
            