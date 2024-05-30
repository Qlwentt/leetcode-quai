class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        # maxes = [2,3,7,7,10]
        # conv =  [4,6,14,12,20]
        # score [4,10,24,36,56]
        
        score = []
        curMax = float('-inf')
        curSum  = 0
        for num in nums:
            curMax = max(num, curMax)
            curSum += curMax + num
            score.append(curSum)
        
        
        return score