class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        
        
        validBoards = []
        board = []
        
        rowTally = [False] * n
        colTally = [False] * n
        xDiagTally = [False] * (((n-1) * 2) +1)
        yDiagTally = [False] * (((n-1) * 2 )+1)
        
        def backtrack(possibleChoices):
            if not possibleChoices:
                validBoards.append(board[:])
                return
            
            for i, queenPosition in enumerate(possibleChoices):
                r = queenPosition
                c = len(board)
                
                if (rowTally[r] or
                    colTally[c] or 
                    xDiagTally[r-c + n - 1] or
                    yDiagTally[r+c]):
                    continue
                
                row = ["."] * n
                row[queenPosition] = "Q"
                row = "".join(row)
                board.append(row)
                
                rowTally[r] = True
                colTally[c] = True
                xDiagTally[r-c + n - 1] = True
                yDiagTally[r+c] = True
                
                backtrack(possibleChoices[:i]+possibleChoices[i+1:])
                
                board.pop()
                rowTally[r] = False
                colTally[c] = False
                xDiagTally[r-c + n - 1] = False
                yDiagTally[r+c] = False
            
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
                    
        
            