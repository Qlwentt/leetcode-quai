from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque([])
        ROWS = len(rooms)
        COLS = len(rooms[0])
        INF = 2**31 -1
        
        # initialize q with gates
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r,c, 0))
                    
                    
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        while q:
            r, c, distance = q.popleft()
            
            for dr, dc in directions:
                new_r = dr + r
                new_c = dc + c
                if (new_r in range(ROWS) and 
                    new_c in range(COLS) and
                   rooms[new_r][new_c] == INF):
                    q.append((new_r, new_c, distance + 1))
                    rooms[new_r][new_c] = distance+1
                    
        
                    
            