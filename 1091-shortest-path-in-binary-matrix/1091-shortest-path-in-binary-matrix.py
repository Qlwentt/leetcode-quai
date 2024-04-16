from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque([])
        if grid[0][0] == 0:
            q.append((0,0, 1, [(0,0)]))
            
        answer = - 1
        directions = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]
        N = len(grid)
        visited = set()
        while q:
            r, c, level, path = q.popleft()
            
            if r == N-1 and c == N-1:
                # print(path)
                return level
            
            for dr, dc in directions:
                newR = dr + r
                newC = dc + c
                if (
                    newR in range(N) and
                    newC in range(N) and
                    (newR, newC) not in visited and
                    grid[newR][newC] != 1
                ):
                    q.append((newR, newC, level+1, path + [(newR,newC)]))
                    visited.add((newR, newC))
        # print([])
        return answer