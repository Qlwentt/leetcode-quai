class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.sumMatrix = [[0] * (COLS + 1) for _ in range(ROWS+1)]
        
        for row in range(ROWS):
            prefixSumRow = 0
            for col in range(COLS):
                prefixSumRow += matrix[row][col]
                r = row + 1
                c = col + 1
                self.sumMatrix[r][c] = self.sumMatrix[r-1][c] + prefixSumRow        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.sumMatrix[row2][col2]
        aboveTopLeft = self.sumMatrix[row1-1][col1-1]
        beforeBottomLeft = self.sumMatrix[row2][col1-1]
        aboveTopRight = self.sumMatrix[row1-1][col2]
        
        return bottomRight - (beforeBottomLeft + aboveTopRight) + aboveTopLeft
        


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)