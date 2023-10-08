from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque([])
        visited = set()
        ROWS = len(rooms)
        COLS = len(rooms[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    q.append((row,col, 0))
                    visited.add((row,col))
                    
        directions = [[0,-1],[0,1],[-1,0],[1,0]]           
        while q:
            r, c, distance = q.popleft()
            rooms[r][c] = distance
            
            for dr, dc in directions:
                row,col = r + dr, c + dc
                if (row in range(ROWS) and col in range(COLS) and
                    (row,col) not in visited and
                    rooms[row][col] != -1
                ):
                    q.append((row, col, distance + 1))
                    visited.add((row,col))
        