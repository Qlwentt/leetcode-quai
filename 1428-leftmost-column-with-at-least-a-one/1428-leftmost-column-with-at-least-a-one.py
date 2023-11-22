# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        def getFirstOne(row, hi):
            lo = 0

            while lo <= hi:
                mid = (lo+hi) // 2
                if binaryMatrix.get(row, mid):
                    hi = mid - 1
                else:
                    lo = mid + 1
            return lo
        
        ROWS , COLS = binaryMatrix.dimensions()
        answer = COLS
        for i in range(ROWS):
            answer = min(getFirstOne(i, min(answer, COLS-1)), answer)
        return answer if answer != COLS else -1
        
       
        
        