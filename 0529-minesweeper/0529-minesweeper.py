class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        ROWS = len(board)
        COLS = len(board[0])
        
        digitBoard = [[0] * COLS for _ in range(ROWS)]
        q = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "M":
                    q.append((r,c,0))
                    
                    
        directions = [[0,1],[1,0], [0,-1], [-1,0], [1,1], [-1,-1], [-1,1], [1,-1]]
     
        while q:
            r,c, level = q.popleft()
            if level == 1:
                digitBoard[r][c] += 1
            lastLevel = level
            for dr,dc in directions:
                newR = dr + r
                newC = dc + c
                if (
                    newR in range(ROWS) and
                    newC in range(COLS) and
                    board[newR][newC] == "E" and level == 0
                ):
                    q.append((newR, newC, level+1))
        # print(digitBoard)   
        visited = set()
        def dfs(r,c):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                (r,c) in visited
            ):
                return 
            visited.add((r,c))
            if board[r][c] == "E":
                if digitBoard[r][c] > 0:
                    board[r][c] = str(digitBoard[r][c])
                else:
                    board[r][c] = "B"
                    dfs(r-1,c)
                    dfs(r+1,c)
                    dfs(r,c-1)
                    dfs(r,c+1)
                    dfs(r+1,c+1)
                    dfs(r-1,c-1)
                    dfs(r+1,c-1)
                    dfs(r-1,c+1)
            
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
        else:
            dfs(click[0], click[1])
        return board