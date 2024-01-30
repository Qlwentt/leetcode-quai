from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        # update grid 1 = "1", 2="2" 0 = infinity
        houses = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    grid[r][c] = (float('inf'), 0)
                else:
                    if grid[r][c] == 1:
                        houses.append([r,c])
                    grid[r][c] = str(grid[r][c])
        
        def bfs(startX, startY):
           
            q = deque([(startX, startY, 0)])
            visited = set((startX, startY))
            directions = [[0,1], [1,0], [0,-1], [-1,0]]
            while q:
                r, c, distance = q.popleft()
                if not isinstance(grid[r][c], str):
                    grid[r][c] = (distance, 1) if grid[r][c][0] == float('inf') else (grid[r][c][0] + distance, grid[r][c][1]+1)
                
                for dr, dc in directions:
                    newR = dr + r
                    newC = dc + c
                    if (
                        newR in range(ROWS) and
                        newC in range(COLS) and
                       (newR, newC) not in visited and
                        isinstance(grid[newR][newC], str) == False
                    ):
                        q.append((newR, newC, distance+1))
                        visited.add((newR, newC))
                
                
            
        for r, c in houses:
            bfs(r,c)
            
        minDistance = float('inf')
        for r in range(ROWS):
            for c in range(COLS):
                if not isinstance(grid[r][c], str) and grid[r][c][1] == len(houses):
                    minDistance = min(minDistance, grid[r][c][0])
                    
        return minDistance if minDistance != float('inf') else -1