from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque([])
        
        if grid[0][0] == 0:
            q.append((0,0,1))
            visited.add((0,0))
        
        directions = [[0,1],[1,0], [0,-1], [-1,0], [1,1], [-1,-1], [-1,1], [1, -1]]
        
        while q:
            r, c, level = q.popleft()
            
            
            if (r,c) == (ROWS-1, COLS-1):
                return level
            
            for dr, dc in directions:
                newR = r + dr
                newC = c + dc
                
                if (newR in range(ROWS) and
                    newC in range(COLS) and
                    (newR, newC) not in visited and
                    grid[newR][newC] != 1
                   ):
                    
                    q.append((newR, newC, level +1))
                    visited.add((newR, newC))
        # print([])
        return -1
        