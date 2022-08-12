class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def powPositive(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if x == 0:
                return 0
            half = self.myPow(x,n//2)
            if n % 2 == 0:
                return half * half
            else:
                return x * half * half

        if n > 0:
            return powPositive(x,n)
        else:
            return powPositive(1/x,-n)