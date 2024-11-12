class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combs = []
        
        def backtrack(i, curComb):
            if len(curComb) == k:
                combs.append(curComb.copy())
                return
           
             
            for j in range(i, n+1):
                curComb.append(j)
                backtrack(j+1, curComb)
                curComb.pop()

        backtrack(1, [])
        return combs