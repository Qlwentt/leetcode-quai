class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        # if n == 1:
        #     return True
        # if n % 3 != 0:
        #     return False
        # return self.isPowerOfThree(n/3)
        if n <= 0:
            return False
        return (math.log10(n) / math.log10(3)) % 1 == 0
        