from collections import defaultdict
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])
        diagNums = defaultdict(set)
        for row in range(numRows):
            for col in range(numCols):
                diagNums[row-col].add(matrix[row][col])
                if len(diagNums[row-col]) > 1:
                    return False
        return True