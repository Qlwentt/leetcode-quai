class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix) - 1
        
        while right > left:
            for i in range(right - left):
                top = left
                bottom = right
                
                topLeft = matrix[top][left + i]
                
                # move bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]
                
                # move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                # move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                
                # move top left into top right
                matrix[top + i][right] = topLeft
                
            right -= 1
            left += 1