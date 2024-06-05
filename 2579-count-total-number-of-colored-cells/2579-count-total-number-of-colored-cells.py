class Solution:
    def coloredCells(self, n: int) -> int:
#         1,5,13
        
#         1,2,3,4
#         1,4,8,12
        # return 4 * n
    
        if n == 1:
            return 1
        answer = 4 * (n -1)
        return answer + self.coloredCells(n-1)
        
        