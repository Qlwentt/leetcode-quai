class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        mat = isWater
        ROWS = len(mat)
        COLS = len(mat[0])
        visited = set()
        q = deque([])
        
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 1:
                    q.append((r,c, 0))
                    visited.add((r,c))
                    
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        while q:
            r,c,distance = q.popleft()
            mat[r][c] = distance
            
            for dr, dc in directions:
                newR = dr + r
                newC = dc + c
                if (newR in range(ROWS) and
                    newC in range(COLS) and
                    (newR, newC) not in visited
                   ):
                    q.append((newR,newC, distance + 1))
                    visited.add((newR,newC))
        return mat