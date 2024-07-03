class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        N = len(mat)
        
        def rotate(mat):
            for r in range(N):
                for c in range(r+1,N):
                    mat[r][c], mat[c][r] = mat[c][r], mat[r][c]
            for row in mat:
                row.reverse()
        def is_same(mat1, mat2):
            N = len(mat1)
            for r in range(N):
                for c in range(N):
                    if mat1[r][c] != mat2[r][c]:
                        return False
            return True
        for _ in range(4):
            if is_same(mat, target):
                return True
            rotate(mat)
        return False