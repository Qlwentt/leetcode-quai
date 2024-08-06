class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        ROWS = len(board)
        COLS = len(board[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                num = board[r][c]
                if num == ".":
                    continue
                if num in rows[r] or num in cols[c] or num in boxes[(r//3, c//3)]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                boxes[(r//3, c//3)].add(num)
        return True
                