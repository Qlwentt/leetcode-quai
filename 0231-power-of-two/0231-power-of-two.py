class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 0
        num = 0
        while num < n:
            num = 2 ** power
            if num == n:
                return True
            power += 1
        return False