# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        ROWS, COLS = binaryMatrix.dimensions()
        result = COLS
        def move(row, col):
            nonlocal result
            if row not in range(ROWS) or col not in range(COLS):
                return
            if binaryMatrix.get(row,col) == 1:
                result = col
                #left
                move(row, col - 1)
            else:
                # up
                move(row-1, col)
        move(ROWS-1,COLS-1)
        return result if result != COLS else -1
            
        
       
        
        