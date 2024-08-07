class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_row():
            top = 0
            bottom = len(matrix) - 1
            
            while top <= bottom:
                mid = (top+bottom) // 2
                if target in range(matrix[mid][0], matrix[mid][-1]+1):
                    return mid
                elif target < matrix[mid][0]:
                    bottom = mid -1
                else: # target > matrix[mid][-1]
                    top = mid + 1
            return -1
        
        def is_in_array(arr):
            l = 0
            r = len(arr) - 1
            
            while l <= r:
                mid = (l+r) // 2
                
                if arr[mid] > target:
                    r = mid - 1
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    return True
            return False
        row = find_row()
        if row == -1:
            return False
        return is_in_array(matrix[row])