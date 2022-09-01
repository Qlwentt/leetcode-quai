from collections import defaultdict
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        #   0 1 2 3
        #0 [1,2,3,4],
        #1 [5,1,2,3],
        #2 [9,5,1,2]
        
        
      # 0,0 1,1 2,2
      # 0,1 1,2 2,3
      # 0,2 1,3
      # 0,3
      # 1,0 2,1
      # 2,0
        
      # 0-0 = 0 1-1 = 0 2-2=0
      # 0-1 = -1 1-2 = -1 2-3 = -1
        numRows = len(matrix)
        numCols = len(matrix[0])
        diagNums = defaultdict(set)
        for row in range(numRows):
            for col in range(numCols):
                diagNums[row-col].add(matrix[row][col])
                if len(diagNums[row-col]) > 1:
                    return False
        return True