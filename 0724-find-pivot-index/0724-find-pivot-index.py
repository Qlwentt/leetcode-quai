class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # [1 ,7 , 3 , 6 ,5 ,6 ]
        # [0 , 1, 8 , 11,17,22]
        # [27,20, 17, 11, 6, 0]
        
        prefixSums = [0] * len(nums)
        postfixSums = [0] * len(nums)
        
        prefixSum = 0
        for i in range(1, len(nums)):
            prefixSum += nums[i-1]
            prefixSums[i] = prefixSum
        
        postfixSum = 0
        for i in range(len(nums)-2, -1, -1):
            postfixSum += nums[i+1]
            postfixSums[i] = postfixSum
            
        for i in range(len(nums)):
            if postfixSums[i] == prefixSums[i]:
                return i
        return -1
        
        