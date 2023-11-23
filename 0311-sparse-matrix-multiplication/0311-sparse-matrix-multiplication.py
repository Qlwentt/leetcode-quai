class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ROWS1, COLS1 = len(mat1), len(mat1[0])
        ROWS2, COLS2 = len(mat2), len(mat2[0])
        
        if COLS1 != ROWS2:
            raise Exception("Invalid matrices")
        # COL1 always equals ROWS2
        
        ansROWS = ROWS1
        ansCOLS = COLS2
        
        answer = [[0]*ansCOLS for row in range(ansROWS)]
        
        for row in range(ansROWS):
            for col in range(ansCOLS):
                for i in range(COLS1):
                    answer[row][col] += mat1[row][i] * mat2[i][col]
        
        return answer
        
        