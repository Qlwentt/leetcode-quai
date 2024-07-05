class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        target = math.prod(nums)
        def get_primes(n):
            def is_prime(n):
                if n <= 1:
                    return False
                
                for i in range(2,int(math.sqrt(n))+1):
                    if n % i == 0:
                        return False
                return True
            primes = []
            for i in range(n+1):
                if is_prime(i):
                    primes.append(i)
            return primes
    
        primes = get_primes(1000)
        factors = []
        for p in primes:
            if target % p == 0:
                factors.append(p)
                
        return len(factors)
        
        
        
                
                    
            