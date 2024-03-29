class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        i = 1
        def getArea(r,c):
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
        idsToArea = {"0": 0}
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = getArea(r,c)
                    idsToArea[str(i)] = area
                    i += 1
        
        largestIsland = float("-inf")
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    directions = [[0,1], [1,0], [-1, 0], [0, -1]]
                    idsForAreas = set()
                    for dr, dc in directions:
                        newR = dr + r
                        newC = dc + c
                        if (
                            newR in range(ROWS) and
                            newC in range(COLS) and
                            isinstance(grid[newR][newC], str)
                        ):
                            idsForAreas.add(grid[newR][newC])
                    totalArea = 1
                    for id_ in idsForAreas:
                        totalArea += idsToArea[id_]
                    largestIsland = max(totalArea, largestIsland)
                    
        return largestIsland if largestIsland != float('-inf') else max(idsToArea.values())
                        
                    