class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = math.ceil(stoneSum/2)
        memo = {}
        def backtrack(i, curTotal):
            if curTotal >= target or i >= len(stones):
                otherHalf = stoneSum - curTotal
                return abs(curTotal - otherHalf)
            
            if (i, curTotal) in memo:
                return memo[(i,curTotal)]
            
            memo[(i,curTotal)] = min(backtrack(i+1, curTotal), backtrack(i+1, curTotal+stones[i]))
            return memo[(i, curTotal)]
        
        return backtrack(0,0)
                    
            
            
            
        