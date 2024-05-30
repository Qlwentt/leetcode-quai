class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        # maxes = [2,3,7,7,10]
        # conv =  [4,6,14,12,20]
        # score [4,10,24,36,56]
        
        maxes = []
        curMax = float('-inf')
        for num in nums:
            curMax = max(num, curMax)
            maxes.append(curMax)
        
        conver = nums.copy()
        for i in range(len(conver)):
            conver[i] = conver[i] + maxes[i]
            
        score = []
        curSum = 0
        for num in conver:
            curSum += num
            score.append(curSum)
            
        return score