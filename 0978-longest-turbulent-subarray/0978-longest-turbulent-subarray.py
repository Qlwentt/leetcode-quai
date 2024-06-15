class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def comp(a,b):
            if a > b:
                return 1
            if a == b:
                return 0
            return -1
   
        L = 0            
        answer = 1       
        for R in range(1,len(arr)):
            c = comp(arr[R-1], arr[R])
            if c == 0:
                L = R
            elif R == len(arr)-1 or c * comp(arr[R], arr[R+1]) != -1:
                answer = max(R-L+1, answer)
                L = R
            
            
        return answer