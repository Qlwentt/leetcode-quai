class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_matrix = defaultdict(int)
        
        for row in range(len(matrix)):
            prefix_row = 0
            for col in range(len(matrix[0])):
                prefix_row += matrix[row][col]
                self.prefix_matrix[(row,col)] = self.prefix_matrix[(row-1,col)] + prefix_row 
        print(self.prefix_matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        cross = self.prefix_matrix[(row1-1,col1-1)]
        left = self.prefix_matrix[(row2, col1-1)]
        top = self.prefix_matrix[(row1-1,col2)]
        bottom_right = self.prefix_matrix[(row2,col2)]        
        return bottom_right - (left+top-cross)
        
        
        


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)