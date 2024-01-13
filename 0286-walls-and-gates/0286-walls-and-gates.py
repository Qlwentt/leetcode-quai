from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque([])
        ROWS = len(rooms)
        COLS = len(rooms[0])
        visited = set()
        # initialize q with gates
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r,c, 0))
                    visited.add((r,c))
                    
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        while q:
            r, c, distance = q.popleft()
            rooms[r][c] = distance
            
            for dr, dc in directions:
                newR = dr + r
                newC = dc + c
                if (newR in range(ROWS) and 
                    newC in range(COLS) and
                    (newR, newC) not in visited and
                   rooms[newR][newC] != -1):
                    q.append((newR, newC, distance + 1))
                    visited.add((newR, newC))
                    
        
                    
            