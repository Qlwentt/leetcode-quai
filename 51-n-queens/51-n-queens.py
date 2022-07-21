class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        
        
        validBoards = []
        board = []
        
        def backtrack(possibleChoices):
            if not possibleChoices  and self.isSolution(board):
                validBoards.append(board[:])
                return
            
            for i, queenPosition in enumerate(possibleChoices):
                row = ["."] * n
                row[queenPosition] = "Q"
                row = "".join(row)
                board.append(row)
                backtrack(possibleChoices[:i]+possibleChoices[i+1:])
                board.pop()
            
        backtrack([i for i in range(n)])
        return validBoards
                
                    
    
    def isSolution(self,board):
        n = len(board)

        rowTally = [0] * n
        colTally = [0] * n
        xDiagTally = [0] * (((n-1) * 2) +1)
        yDiagTally = [0] * (((n-1) * 2 )+1)
        
        for row in range(n):
            for col in range(n):
                if board[row][col] == "Q":
                    rowTally[row] += 1
                    colTally[col] += 1
                    xDiagTally[row - col + n -1] += 1
                    yDiagTally[row+col] += 1
        
                    if (rowTally[row] > 1 or
                        colTally[col] > 1 or
                        xDiagTally[row-col + n - 1] > 1 or
                        yDiagTally[row+col] > 1):
                        return False
        return True
                    
        
            