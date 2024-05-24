import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        power = int(math.log2((n)))
        return 2 ** power == n
        