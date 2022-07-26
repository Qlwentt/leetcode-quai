from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = set()
        
        numRows = len(grid)
        numCols = len(grid[0])
        
        q = deque([])
        minutes = 0
        
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 1:
                    fresh.add((r,c))
                if grid[r][c] == 2:
                    q.append((r,c,0))
                    
        while q:
            r,c, time = q.popleft()
            if (r < 0 or c < 0 or
                r >= numRows or
                c >= numCols or
                grid[r][c] == 0 or
                (r,c) in rotten
            ):
                continue
            minutes = time
            
            rotten.add((r,c))
            if (r,c) in fresh:
                fresh.remove((r,c))
            
            q.append((r + 1,c,time+1))
            q.append((r - 1,c,time+1))
            q.append((r,c + 1,time+1))
            q.append((r,c - 1,time+1))
        
        return -1 if fresh else minutes
            
        
                
            