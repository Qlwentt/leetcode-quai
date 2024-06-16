class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ROWS = len(strs)
        COLS = len(strs[0])
        
        grid = [[0] * COLS for _ in range(ROWS) ]
        for r in range(ROWS):
            for c in range(COLS):
                grid[r][c] = strs[r][c]
        
        count = 0
        for c in range(COLS):
            prev = float('-inf')
            for r in range(ROWS):
                if ord(grid[r][c]) < prev:
                    count += 1
                    break
                prev = ord(grid[r][c])
        return count