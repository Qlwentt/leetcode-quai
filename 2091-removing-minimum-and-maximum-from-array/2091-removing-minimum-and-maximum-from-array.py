class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        n = len(nums)
        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))
                
        minRemoveMin = min(minIndex+1, n - minIndex) 
        minRemoveMax = min(maxIndex+1, n - maxIndex)
        
        if minRemoveMin == minIndex +1 and minRemoveMax == maxIndex+1:
            return max(minIndex+1, maxIndex+1)
        if n - minIndex == minIndex and n - maxIndex == maxIndex:
            return max(n - minIndex, n - maxIndex)
        return min(minRemoveMin + minRemoveMax, max(minIndex+1, maxIndex+1), max(n - minIndex, n - maxIndex))
