class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                top = r - 1
                left = c - 1
                if top in range(ROWS) and left in range(COLS):
                    if matrix[r][c] != matrix[top][left]:
                        return False
                    
        return True
    
# Time: O(N * M)
# Space: O(1)