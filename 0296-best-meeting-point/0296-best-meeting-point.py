class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        houses = []
        rowHouses = []
        colHouses = []
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    houses.append((r,c))
                    rowHouses.append(r)
                    
        for c in range(COLS):
            for r in range(ROWS):
                if grid[r][c] == 1:
                    colHouses.append(c)
        
        medianRows = rowHouses[len(rowHouses) // 2]
        medianCols = colHouses[len(colHouses) // 2]
        
        distance = 0
        for x1,y1 in houses:
            distance += abs(x1-medianRows) + abs(y1-medianCols)

        return distance