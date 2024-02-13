from collections import defaultdict
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        i = 1
        areas = defaultdict(int)
        areas["0"] = 0
        def getArea(r, c):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or 
                isinstance(grid[r][c], str) or
                grid[r][c] == 0
            ):
                return 0
            
            grid[r][c] = str(i)
            
            up = getArea(r-1, c)
            down = getArea(r+1, c)
            left = getArea(r, c-1)
            right = getArea(r, c+1)
            
            return up + down + left + right + 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = getArea(r,c)
                    areas[str(i)] = area
                    i += 1
        directions = [[0,1],[1,0], [-1,0], [0, -1]]    
        answer = float('-inf')
        for r in range(ROWS):
            for c in range(COLS):
                ids = set()
                if grid[r][c] == 0:
                    for dr, dc in directions:
                        newR, newC = dr + r, dc + c
                        if newR in range(ROWS) and newC in range(COLS):
                            ids.add(grid[r+dr][c+dc])
                    sumAreas = 0
                    for id_ in ids:
                        sumAreas += areas[id_]
                    answer = max(sumAreas+1, answer)                    
                
        return answer if answer != float('-inf') else max(areas.values())
                