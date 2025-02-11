class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # any number xORed with itself is 0
        # xOR all the numbers and the number left is the answer
        result = 0
        for num in nums:
            result = result ^ num
        return result

# Time: O(N)
# Space: O(1)
      
