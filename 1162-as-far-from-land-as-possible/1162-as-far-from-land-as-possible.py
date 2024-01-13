from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        q = deque([])
        
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    q.append((r,c, r,c))
                    visited.add((r,c))
        maxDist = -1
        directions = [[0,1],[1,0], [0,-1], [-1,0]]
        while q:
            x0,y0,x1,y1 = q.popleft()
            distance = abs(x0 - x1) + abs(y0 - y1) if grid[x0][y0] == 0 else -1
            maxDist = max(maxDist, distance)
            
            for dr, dc in directions:
                newX, newY = dr + x0, dc + y0
                if (newX in range(N) and
                    newY in range(N) and
                    (newX, newY) not in visited
                   ):
                    q.append((newX,newY, x1,y1))
                    visited.add((newX, newY))
        return maxDist
            
            
        