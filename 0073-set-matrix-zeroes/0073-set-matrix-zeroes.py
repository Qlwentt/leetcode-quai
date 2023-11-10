class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        def dfs(row,col,direction):
            if (
                row not in range(ROWS) or
                col not in range(COLS) 
            ):
                return
            
            if matrix[row][col] != 0:
                matrix[row][col] = "0"
            
            if direction == "up":
                dfs(row-1, col, "up")
            elif direction == "down":
                dfs(row+1, col, "down")
            elif direction == "left":
                dfs(row, col-1, "left")
            else:
                dfs(row, col+1, "right")
            return 
        
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    dfs(row,col,"up")
                    dfs(row,col,"down")
                    dfs(row,col,"left")
                    dfs(row,col,"right")
                    matrix[row][col] = "0"

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == "0":
                    matrix[row][col] = 0
            
            
            