class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
#         1000   010
#         0011   110
#     ----------
#         0101   101
       
        flips = 0
        
        while a or b or c:
            if c & 1:
                flips +=  not ((a&1) or (b&1))
            else:
                flips += (a&1) + (b&1)
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return flips
            