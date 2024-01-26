class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        idsToArea = {0:0}
        def getArea(r,c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] != 1
               ):
                return 0
            
            grid[r][c] = id_
            
            up = getArea(r-1, c)
            down = getArea(r+1, c)
            left = getArea(r, c-1)
            right = getArea(r, c+1)
            
            
            return up + down + left + right + 1
        
        id_ = -1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = getArea(r,c)
                    idsToArea[id_] = area
                    id_ -= 1
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                islandIds = set()
                if grid[r][c] == 0:
                    for dr, dc in directions:
                        newR = dr + r
                        newC = dc + c
                        if (newR in range(ROWS) and
                            newC in range(COLS) and
                            grid[newR][newC] in idsToArea
                           ):
                            islandIds.add(grid[newR][newC])
                    area = 1
                    for idWithArea in islandIds:
                        area += idsToArea[idWithArea]
                    maxArea = max(maxArea, area)
                    
        return max(maxArea, max(idsToArea.values()))
                    
# Time: O(N^2) hit each element in N*N grid once
# O(N^2) space for recursive DFS 
                    
        
            
        