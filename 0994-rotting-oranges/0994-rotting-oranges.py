from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque([])
        numFresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c, 0))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    numFresh += 1
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        minMins = 0
        while q:
            r,c,time = q.popleft()
            minMins = max(minMins, time)
            numFresh -= grid[r][c] == 1
            
            for dr, dc in directions:
                newR = dr + r
                newC = dc + c
                if (newR in range(ROWS) and
                    newC in range(COLS) and
                    (newR, newC) not in visited and
                    grid[newR][newC] != 0):
                    q.append((newR,newC, time+1))
                    visited.add((newR,newC))

        return minMins if numFresh == 0 else -1
            
            
        
        