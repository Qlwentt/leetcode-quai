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
                newR = dr + r
                newC = dc + c
                if (newR in range(ROWS) and 
                    newC in range(COLS) and
                   rooms[newR][newC] == INF):
                    q.append((newR, newC, distance + 1))
                    rooms[newR][newC] = distance+1
                    
        
                    
            