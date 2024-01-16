class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majEle = None
        majCount = 0
        for num in nums:
            if majCount == 0:
                majEle = num
            if num == majEle:
                majCount += 1
            else:
                majCount -= 1
        
        return majEle
            