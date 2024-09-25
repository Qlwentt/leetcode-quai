class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n >= 2:
            return self.isPowerOfTwo(n/2)
        return True if n == 1 else False
# Time: O(log(N))
# Space: O(log(N))

# Math solution that is technically log(N)because log function takes log(N)Time
        # if n <= 0:
        #     return False
        # power = int(math.log2((n)))
        # return 2 ** power == n
# Time: O(log(N))
# Space: O(1)
        