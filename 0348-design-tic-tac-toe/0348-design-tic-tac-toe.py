class TicTacToe:

    def __init__(self, n: int):
        self.board = {
            "rows": [0] * n,
            "cols": [0] * n,
            "posDiag": 0,
            "negDiag": 0
        }
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        player = 1 if player == 1 else -1
        
        # mark move
        self.board["rows"][row] += player
        self.board["cols"][col] += player
        if row == col:
            self.board["posDiag"] += player
        if row + col == self.n -1:
            self.board["negDiag"] += player
        
        return self.getWinner()
    
    def getWinner(self):
        def getWinRowCol(rowOrCol):
            for tallys in self.board[rowOrCol]:
                if abs(tallys) == self.n:
                    return tallys
            return None
        
        def getWinDiag(diag):
            if abs(self.board[diag]) == self.n:
                return self.board[diag]
            else:
                return None
        results = [getWinRowCol("rows"), getWinRowCol("cols"), getWinDiag("posDiag"), getWinDiag("negDiag")]
        winner = next((item for item in results if item is not None), None)
        if winner == None:
            return 0
        elif winner > 0:
            return 1
        else:
            return 2
                

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)