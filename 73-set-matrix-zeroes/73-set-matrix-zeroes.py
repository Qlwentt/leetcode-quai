class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        def zerosRight(row,col):
            for i in range(row+1,n):
                if matrix[i][col] != 0:
                    matrix[i][col] = "0"
        
        def zerosLeft(row,col):
            for i in range(row-1, -1,-1):
                if matrix[i][col] != 0:
                    matrix[i][col] = "0"
                
        def zerosDown(row,col):
            for i in range(col+1,m):
                if matrix[row][i] != 0:
                    matrix[row][i] = "0"
        
        def zerosUp(row,col):
            for i in range(col-1, -1,-1):
                if matrix[row][i] != 0:
                    matrix[row][i] = "0"
            
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    zerosLeft(row,col)
                    zerosRight(row,col)
                    zerosDown(row,col)
                    zerosUp(row,col)
        
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == "0":
                    matrix[row][col] = 0
                    