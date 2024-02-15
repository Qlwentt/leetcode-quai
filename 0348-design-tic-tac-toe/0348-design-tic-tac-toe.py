from collections import defaultdict
class TicTacToe:

    def __init__(self, n: int):
        self.rows = defaultdict(int) # key = row # value = tally of x vs 0
        self.cols = defaultdict(int)
        self.posDiag = 0
        self.negDiag = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        mark = 1 if player == 1 else -1
        
        self.rows[row] += mark
        self.cols[col] += mark
        if row == col:
            self.posDiag += mark
        if row + col == self.n - 1:
            self.negDiag += mark
            
        if (abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.posDiag) == self.n or
            abs(self.negDiag) == self.n):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)