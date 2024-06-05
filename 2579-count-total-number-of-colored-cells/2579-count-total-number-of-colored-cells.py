class Solution:
    def coloredCells(self, n: int) -> int:
#         1,5,13
        
#         1,2,3,4
#         1,4,8,12
        
        # recursive
        # if n == 1:
        #     return 1
        # answer = 4 * (n -1)
        # return answer + self.coloredCells(n-1)
        
        # iterative
        answer = 0
        prev = 1
        for i in range(n):
            answer = 4 * i + prev
            prev = answer
        
        return answer
        
        