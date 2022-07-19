class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLen = len(board)
        colLen = len(board[0])
        path = set()
        
        def dfs(i, row, col):
            if i == len(word):
                return True
            if ( row < 0 or col < 0 or
                 row >= rowLen or col >= colLen
                 or word[i] != board[row][col]
                 or (row, col) in path
               ):
                return False
            path.add((row,col))
            res = (dfs(i+1, row + 1, col) or
                   dfs(i+1, row - 1, col) or
                   dfs(i+1, row, col + 1) or
                   dfs(i+1, row, col - 1)
                  )
            path.remove((row,col))
            return res
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(0, r, c):
                    return True
                
        return False
    