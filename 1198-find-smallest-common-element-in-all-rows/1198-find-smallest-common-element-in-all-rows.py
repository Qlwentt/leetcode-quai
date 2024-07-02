class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        counts = collections.defaultdict(int)
        
        for row in mat:
            for num in row:
                counts[num] += 1
        
        for num in mat[0]:
            if counts[num] == len(mat):
                return num
        return -1
            