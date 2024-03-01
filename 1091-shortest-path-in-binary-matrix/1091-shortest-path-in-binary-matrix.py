from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        q = deque([(0,0,1)])
        
        if grid[0][0] == 1:
            return -1
        directions = [[0,1],[1,0], [0,-1], [-1,0], [1,1], [-1,-1], [-1, 1], [1, -1]]
        visited = set()
        while q:
            r,c, distance = q.popleft()
            
            if r == N - 1 and c == N -1:
                return distance
            
            for dr, dc in directions:
                newR = dr + r
                newC = dc + c
                if (
                    newR in range(N) and
                    newC in range(N) and
                    grid[newR][newC] != 1 and
                    (newR, newC) not in visited
                ):
                    q.append((newR, newC, distance + 1))
                    visited.add((newR, newC))
                    
        return -1
        