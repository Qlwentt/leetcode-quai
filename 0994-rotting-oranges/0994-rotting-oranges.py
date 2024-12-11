from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque([])
        num_fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c, 0))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    num_fresh += 1
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        answer = 0
        while q:
            r,c,time = q.popleft()
            answer = max(answer, time)
            
            for dr, dc in directions:
                new_r = dr + r
                new_c = dc + c
                if (new_r in range(ROWS) and
                    new_c in range(COLS) and
                    (new_r, new_c) not in visited and
                    grid[new_r][new_c] == 1):
                    q.append((new_r,new_c, time+1))
                    visited.add((new_r,new_c))
                    num_fresh -= 1

        return answer if num_fresh == 0 else -1
    # Time: O(N*M)
    # Space: O(N*M)
        
        