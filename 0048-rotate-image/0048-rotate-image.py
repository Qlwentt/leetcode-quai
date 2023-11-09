class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # row becomes column, col becomes row (transpose)
        # reverse
        
        N = len(matrix)
        
        offset = 0
        for row in range(N):
            for col in range(offset, N):
                matrix[row][col] , matrix[col][row] = matrix[col][row], matrix[row][col]
            offset += 1
        for row in matrix:
            row.reverse()
            
            
        
        