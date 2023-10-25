class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        answer = 1
        memo = {}
        def dfs(row, col, prev):
            if (row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                matrix[row][col] <= prev):
                return 0
            if (row,col) in memo:
                return memo[(row,col)]
            cur = matrix[row][col]
            up = 1 + dfs(row-1, col, cur)
            down = 1+ dfs(row+1, col, cur)
            left = 1 + dfs(row, col-1, cur)
            right = 1 + dfs(row, col+1, cur)
            
            memo[(row,col)] = max(up, down, left, right)
            return memo[(row,col)]
        
        for row in range(ROWS):
            for col in range(COLS):
                answer = max(dfs(row,col, float('-inf')), answer)
                
        return answer