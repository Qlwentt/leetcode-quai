class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        cur_xor = 0
        answer = []
        for num in nums:
            cur_xor ^= num
            k = ((2 ** maximumBit) - 1)^(cur_xor &(2 ** maximumBit) - 1)
            answer.append(k)
        return answer[::-1]