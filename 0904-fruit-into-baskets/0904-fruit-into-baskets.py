class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
       # [1,1,2,3,2,2]  set: <2,3
       #      L
       #            R
       # [3,3,3,1,2,1,1,2,3,3,4]
       #        L
       #                  R
    
        L = 0
        R = 0
        fruitDict = {} # 1 2 3
        maxFruits = float("-inf") # 1 2 3 4 5
        
        while R < len(fruits):
            
            fruitDict[fruits[R]] = fruitDict.get(fruits[R], 0) + 1
            while len(fruitDict) > 2:
                fruitDict[fruits[L]] -= 1
                if not fruitDict[fruits[L]]:
                    del fruitDict[fruits[L]]
                L += 1
    
            maxFruits = max(maxFruits, R-L+1)
            R += 1
        return maxFruits
                