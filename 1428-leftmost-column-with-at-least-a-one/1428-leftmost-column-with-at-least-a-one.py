# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        def getFirstOne(row):
            lo = 0
            hi = COLS - 1

            while lo <= hi:
                mid = (lo+hi) // 2
                if binaryMatrix.get(row, mid):
                    hi = mid - 1
                else:
                    lo = mid + 1
            return lo if lo in range(COLS) else float("inf") 
        
        ROWS , COLS = binaryMatrix.dimensions()
        answer = float("inf")
        for i in range(ROWS):
            answer = min(getFirstOne(i), answer)
        return answer if answer != float("inf") else -1
        
       
        
        