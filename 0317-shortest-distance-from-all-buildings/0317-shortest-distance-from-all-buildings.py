from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        buildings = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    if grid[r][c] == 1:
                        buildings.append((r,c))
                    grid[r][c] = str(grid[r][c])
                else:
                    grid[r][c] = (0,0)
                    
        def bfs(startR, startC):
            visited = set()
            q = deque([(startR, startC, 0)])
            directions = [[0,1],[1,0], [0,-1], [-1,0]]
            while q:
                r,c,distance = q.popleft()
                if grid[r][c] != "1":
                    grid[r][c] = (grid[r][c][0] + distance, grid[r][c][1] + 1)
                
                for dr, dc in directions:
                    newR = dr + r
                    newC = dc + c
                    if (
                        newR in range(ROWS) and
                        newC in range(COLS) and
                        (newR, newC) not in visited and
                        not isinstance(grid[newR][newC], str)
                    ):
                        q.append((newR, newC, distance + 1))
                        visited.add((newR,newC))
        for r, c in buildings:
            bfs(r,c)
        minDistance = float('inf')
        for r in range(ROWS):
            for c in range(COLS):
                if not isinstance(grid[r][c], str) and grid[r][c][1] == len(buildings):
                    minDistance = min(grid[r][c][0], minDistance)
        
        return minDistance if minDistance != float('inf') else -1
                    
                
            
            
        