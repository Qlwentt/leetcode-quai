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
        p = 1 if player == 1 else -1
        
        # mark move
        self.board["rows"][row] += p
        self.board["cols"][col] += p
        if row == col:
            self.board["posDiag"] += p
        if row + col == self.n -1:
            self.board["negDiag"] += p
        
        if (abs(self.board["rows"][row]) == self.n or
            abs(self.board["cols"][col]) == self.n or
            abs(self.board["posDiag"]) == self.n or
            abs(self.board["negDiag"]) == self.n
           ):
            return player
        return 0
                

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)