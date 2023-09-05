class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearchMatrix(matrix):
            lo = 0
            hi = len(matrix) -1
            
            while lo <= hi:
                mid = (lo + hi) // 2
                if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                    return matrix[mid]
                elif target < matrix[mid][0]:
                    hi = mid - 1
                elif target > matrix[mid][0]:
                    lo = mid + 1
                else:
                    return False
            
     #         lo           mid            hi
        # [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        
        
        def binarySearchArr(arr):
            L = 0
            R = len(arr) - 1
            
            [1,3,5,7]
        #    L
        #          R
        #        M
            
            while L <= R:
                mid = (L+R) // 2
                if arr[mid] == target:
                    return True
                elif target < arr[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            return False
        
        targetArr = binarySearchMatrix(matrix)
        return binarySearchArr(targetArr) if targetArr else targetArr