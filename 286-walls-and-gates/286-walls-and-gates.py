from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        numRows = len(rooms)
        numCols = len(rooms[0])
        visited = set()
        q = deque([])
        
        for r in range(numRows):
            for c in range(numCols):
                if rooms[r][c] == 0:
                    q.append((r,c, 0))
        
        while q:
            r, c, distance = q.popleft()
            if (
                r < 0 or c < 0 or
                r >= numRows or
                c >= numCols or
                (r,c) in visited or
                rooms[r][c] == -1
            ):
                continue
                
            rooms[r][c] = distance
            visited.add((r,c))

            q.append((r+1,c,distance +1))
            q.append((r-1,c,distance +1))
            q.append((r,c+1,distance +1))
            q.append((r,c-1,distance +1))
        