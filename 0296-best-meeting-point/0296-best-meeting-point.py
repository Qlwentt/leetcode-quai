class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        housesRows = []
        ROWS = len(grid)
        COLS = len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    housesRows.append(r)
        housesCols = []
        for c in range(COLS):
            for r in range(ROWS):
                if grid[r][c] == 1:
                    housesCols.append(c)
                   
        medianR = housesRows[len(housesRows) // 2]
        medianC = housesCols[len(housesCols) // 2]
        distance = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    distance += abs(medianR-r) + abs(medianC - c)
        return distance