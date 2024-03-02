class TicTacToe:

    def __init__(self, n: int):
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.posDiag = 0
        self.negDiag = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        p = 1 if player == 1 else -1
        self.rows[row] += p
        self.cols[col] += p
        if row == col:
            self.posDiag += p
        if row + col == self.n - 1:
            self.negDiag += p
            
        if (
            abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.posDiag) == self.n or
            abs(self.negDiag) == self.n
        ):
            return player
        return 0
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)