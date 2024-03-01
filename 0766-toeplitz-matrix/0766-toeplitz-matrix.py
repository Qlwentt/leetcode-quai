class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if r+1 in range(ROWS) and c + 1 in range(COLS):
                    if matrix[r][c] != matrix[r+1][c+1]:
                        return False
        return True
        