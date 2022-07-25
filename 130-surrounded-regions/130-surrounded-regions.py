class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        numRows = len(board)
        numCols = len(board[0])
        visited = set()
        toKeep = set()
        
        def markToKeep(r,c):
            if (r < 0 or c < 0 or
                r >= numRows or
                c >= numCols or
                (r,c) in toKeep or
                board[r][c] == "X"
            ):
                return
            toKeep.add((r,c))
            
            
            markToKeep(r + 1,c)
            markToKeep(r - 1,c)
            markToKeep(r,c + 1)
            markToKeep(r,c - 1)
        
        for r in range(numRows):
            for c in range(numCols):
                if (r == 0 or c == 0 or
                    r == numRows - 1 or
                    c == numCols - 1):
                        if board[r][c] == "O":
                            markToKeep(r,c)
        
        for r in range(numRows):
            for c in range(numCols):
                if board[r][c] == "O" and (r,c) not in toKeep:
                    board[r][c] = "X"
                    

            