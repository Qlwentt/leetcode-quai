class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_row():
            top = 0
            bottom = len(matrix) - 1
            
            while top <= bottom:
                mid = (top+bottom) // 2
                if target < matrix[mid][0]:
                    bottom = mid -1
                elif target > matrix[mid][-1]:
                    top = mid + 1
                else:# target >= matrix[mid][0] and target <= matrix[mid][-1]
                    return mid
            return -1
        
        def find_col(row):
            l = 0
            r = len(row) - 1
            
            while l <= r:
                mid = (l+r) // 2
                
                if row[mid] > target:
                    r = mid - 1
                elif row[mid] < target:
                    l = mid + 1
                else:
                    return True
            return False
        row = find_row()
        if row == -1:
            return False
        return find_col(matrix[row])