class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # row becomes column, col becomes row (transpose)
        # reverse
        
#         N = len(matrix)
        
#         offset = 0
#         for row in range(N):
#             for col in range(offset, N):
#                 matrix[row][col] , matrix[col][row] = matrix[col][row], matrix[row][col]
#             offset += 1
#         for row in matrix:
#             row.reverse()

        # rotate one by one
        N = len(matrix)
        TOP = 0
        BOT = N - 1
        while TOP < BOT:
            L = TOP
            R = BOT
            for offset in range(R-L):
                topLeft = matrix[TOP][L+offset]
                topRight = matrix[TOP+offset][R]
                botLeft = matrix[BOT-offset][L]
                botRight = matrix[BOT][R-offset]
                # rotate
                # top left goes to top right
                # top right goes to bottom right
                # bottom right goes to bottom left
                # bottom left goes to top left

                matrix[TOP+offset][R] = topLeft
                matrix[BOT][R-offset] = topRight
                matrix[BOT-offset][L] = botRight
                matrix[TOP][L+offset] = botLeft
                offset += 1
            TOP += 1
            BOT -= 1
        
                
                
        
            
            
        
        