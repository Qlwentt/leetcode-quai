class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        target = math.prod(nums)
        def get_primes(n):
            primes = [True] * (n+1)
            primes[0] = False
            primes[1] = False
            
            for i in range(2,len(primes)):
                if primes[i]:
                    for j in range(i+i, len(primes), i):
                        primes[j] = False
            
            return [i for i, is_prime in enumerate(primes) if is_prime == True]
    
        primes = get_primes(1000)
        factors = []
        for p in primes:
            if target % p == 0:
                factors.append(p)
                
        return len(factors)
        
        
        
                
                    
            