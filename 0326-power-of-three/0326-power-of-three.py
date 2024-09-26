class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # recursive solution
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n/3)
# Time: O(log(N)) (base 3)
# Space: O(log(N)) (base 3)        
        
        # optimized math solution
        # return true if log base 3 of n is an integer
        if n <= 0:
            return False
        return (math.log10(n) / math.log10(3)) % 1 == 0 

# Time: O(1) in python (depends on time complexity of log library function)
# Space: O(1)

        