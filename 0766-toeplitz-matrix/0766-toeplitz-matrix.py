class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                item = matrix[row][col]
                top = row - 1
                left = col - 1
                if top in range(ROWS) and left in range(COLS):
                    if matrix[top][left] != item:
                        return False
                
        return True