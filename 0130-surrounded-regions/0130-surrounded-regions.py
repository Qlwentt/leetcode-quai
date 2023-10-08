class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        
        dontFlip = set()
        
        # mark all ones you shouldn't flip
        def dfs(row,col):
            if (row < 0 or col < 0 or 
                row >= ROWS or col >= COLS or
                board[row][col] == "X" or
                (row,col) in dontFlip
               ):
                return
            
            dontFlip.add((row,col))
        
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
        
        # run dfs to find all the ones you shouldn't flip
        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS-1,c)
        
        for r in range(ROWS):
            dfs(r,0)
            dfs(r, COLS-1)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row,col) not in dontFlip:
                    board[row][col] = "X"
        
                
        