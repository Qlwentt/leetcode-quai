class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        
        @cache
        def isPrime(num):
            if num <= 1:
                return False
            
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    return False
            return True
        
        
        L = None
        for i, num in enumerate(nums):
            if isPrime(num):
                L = i
                break
        
        for i, num in reversed(list(enumerate(nums))):
            if isPrime(num):
                R = i
                break
               
        return R - L
            
                
                        
        