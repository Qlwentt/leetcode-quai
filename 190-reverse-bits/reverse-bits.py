class Solution:
    def reverseBits(self, n: int) -> int:
        power = 31
        answer = 0
        while n:
            if n & 1:
                answer += 2 ** power
            power -= 1
            n = n >> 1
        return answer

# Time: O(32) -> O(1)
# Space: O(1)