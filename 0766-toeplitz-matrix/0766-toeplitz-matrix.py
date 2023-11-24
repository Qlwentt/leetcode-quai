class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diag = {}
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                item = matrix[row][col]
                existing = diag.get(row-col, None)
                if existing != None and existing != item:
                    return False
                diag[row-col] = item
        return True