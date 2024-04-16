class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS = len(mat)
        COLS = len(mat[0])
        
        r = 0
        c = 0
        answer = []
        while r in range(ROWS) and c in range(COLS):
            while r in range(ROWS) and c in range(COLS):
                answer.append(mat[r][c])
                r -= 1
                c += 1
            r += 1
            c -= 1
            if c + 1 in range(COLS):
                c += 1
            else:
                r += 1
            while r in range(ROWS) and c in range(COLS):
                answer.append(mat[r][c])
                r += 1
                c -= 1
            r -= 1
            c += 1
            if r + 1 in range(ROWS):
                r += 1
            else:
                c += 1
        
        return answer