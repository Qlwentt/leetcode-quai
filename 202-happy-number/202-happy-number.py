class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1:
            seen.add(n)
            n = sum([int(digit)**2 for digit in str(n)])
            if n in seen:
                return False         
        return True