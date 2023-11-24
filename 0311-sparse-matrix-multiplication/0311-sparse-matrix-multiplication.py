class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        A = []
        B = []
        
        ROWS1 = len(mat1)
        COLS1 = len(mat1[0])
        
        ROWS2 = len(mat2)
        COLS2 = len(mat2[0])
        
        for row in range(ROWS1):
            curRow = []
            for col in range(COLS1):
                if mat1[row][col] != 0:
                    curRow.append((col, mat1[row][col]))
            A.append(curRow)
            
        for row in range(ROWS2):
            curRow = []
            for col in range(COLS2):
                if mat2[row][col] != 0:
                    curRow.append((col, mat2[row][col]))
            B.append(curRow)
        
        answer = [[0]*COLS2 for _ in range(ROWS1)]
        
        for row in range(ROWS1):
            for col1, ele1 in A[row]:
                for col2, ele2 in B[col1]:
                    answer[row][col2] += ele1 * ele2
        return answer   
        
        
        