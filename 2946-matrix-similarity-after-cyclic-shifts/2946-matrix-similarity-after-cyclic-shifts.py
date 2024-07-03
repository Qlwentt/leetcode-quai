class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        ROWS = len(mat)
        COLS = len(mat[0])
        
        k = k % COLS
        shifted = mat.copy()
        while k:
            for i, row in enumerate(shifted):
                if i % 2:
                    shifted[i] = [row[-1]] + row[:-1]
                else:
                    shifted[i] = row[1:] + [row[0]]
            k -= 1
                    
        for r in range(ROWS):
            for c in range(COLS):
                if shifted[r][c] != mat[r][c]:
                    return False
        return True
            