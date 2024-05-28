class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isPrime(num):
            if num <= 1:
                return False
            
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    return False
            return True
        
        maxDistance = 0
        L = 0
        for R in range(len(nums)):
            while not isPrime(nums[L]):
                L += 1
            if isPrime(nums[R]):
                maxDistance = max(R-L, maxDistance)
        return maxDistance
            
                
                        
        