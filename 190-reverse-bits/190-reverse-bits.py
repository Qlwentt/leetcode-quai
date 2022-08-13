class Solution:
    def reverseBits(self, n: int) -> int:
        number = 0
        power = 31
        while n:
            if n & 1:
                number += 1 * 2**power
            n = n >> 1
            power -= 1
            
        return number