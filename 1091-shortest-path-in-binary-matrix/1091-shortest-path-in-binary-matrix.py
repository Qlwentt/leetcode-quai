from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = set([(0,0)])
        q = deque([(0,0,1)])
        while q:
            r,c,level = q.popleft()
            if grid[r][c] == 1:
                continue
            if r == ROWS - 1 and c == COLS - 1:
                return level
            # up, down, left, right, up+left, up+right, down+left, down+right
            directions = [[-1, 0], [1,0], [0,-1], [0,1], [-1,-1], [1,1], [-1,1], [1,-1]]
            for dr, dc in directions:
                newRow = dr + r
                newCol = dc + c
                if (newRow in range(ROWS) and 
                    newCol in range(COLS) and
                    (newRow,newCol) not in visited and
                    grid[newRow][newCol] == 0
                   ):
                    q.append((newRow, newCol, level+1))
                    visited.add((newRow, newCol))
                    
            
        return -1
            