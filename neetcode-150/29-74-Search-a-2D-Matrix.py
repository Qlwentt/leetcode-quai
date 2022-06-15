from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowsN = len(matrix)
        colsM = len(matrix[0])
        
        top = 0
        bottom = rowsN - 1
        
        foundRow = False
        while bottom >= top:
            row = top + (bottom - top) // 2
            if target >= matrix[row][0] and target <= matrix[row][-1]:
                foundRow = True
                break
            elif target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
        
        if not foundRow:
            return False
        
        l = 0
        r = colsM - 1
        
        while r >= l:
            mid = l + (r - l) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else: # found
                return True
        return False

# O(log(m) + log(n)) time
# O(1) space