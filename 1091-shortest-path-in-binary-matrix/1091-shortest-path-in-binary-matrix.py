from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque([])
        if grid[0][0] != 1:
            q.append((0,0,1))
        visited = set([(0,0)])
        n = len(grid)
        
        directions = [[0,1],[1,0],[-1,0],[0,-1],[1,1], [-1,-1], [-1,1],[1,-1]]
        answer = -1
        while q:
            r, c, level = q.popleft()
            
            if (r,c) == (n-1,n-1):
                return level
            
            for dr, dc in directions:
                newR, newC = dr + r, dc + c
                if (newR in range(n) and
                    newC in range(n) and
                    (newR,newC) not in visited and
                    grid[newR][newC] != 1
                   ):
                    q.append((newR,newC, level+1))
                    visited.add((newR, newC))
        return answer
                    