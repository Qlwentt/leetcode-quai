class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        result = []
        while right > left and bottom > top:
            # get the first row
            for i in range(left, right):
                result.append(matrix[top][i])
                
            top += 1
            
            # get the last col
            for i in range(top, bottom):
                result.append(matrix[i][right -1])
            right -= 1
        
            if not(right > left and bottom > top):
                break
            
            # get the bottom row
            for i in range(right-1, left -1, -1):
                result.append(matrix[bottom -1][i])
            bottom -= 1
            
            # get the first col
            for i in range(bottom -1, top -1, -1):
                result.append(matrix[i][left])
            
            left += 1
        return result