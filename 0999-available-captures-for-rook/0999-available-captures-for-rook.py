class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        captures = 0
        rook_position = [None,None]
        ROWS = len(board)
        COLS = len(board[0])
        answer = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "R":
                    rook_position = [r,c]
                    break
        
        # up
        r,c = rook_position
        while r - 1 in range(ROWS) and board[r-1][c] in [".", "p"]:
            r -= 1
            if board[r][c] == "p":
                answer += 1
                break
        
        # down
        r,c = rook_position
        while r + 1 in range(ROWS) and board[r+1][c] in [".", "p"]:
            r += 1
            if board[r][c] == "p":
                answer += 1
                break
        
        # left
        r,c = rook_position
        while c - 1 in range(COLS) and board[r][c-1] in [".", "p"]:
            c -= 1
            if board[r][c] == "p":
                answer += 1
                break
        
        # right        
        r,c = rook_position
        while c + 1 in range(COLS) and board[r][c+ 1] in [".", "p"]:
            c += 1
            if board[r][c] == "p":
                answer += 1
                break
        
        return answer
                
        
                
        

        
        
        
        