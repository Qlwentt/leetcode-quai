class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        rows_dict = collections.defaultdict(int)
        cols_dict = collections.defaultdict(int)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    rows_dict[r] += 1
                    cols_dict[c] += 1
        answer = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (rows_dict[r] > 1 or cols_dict[c] > 1):
                    answer += 1
        
        return answer
                    
        