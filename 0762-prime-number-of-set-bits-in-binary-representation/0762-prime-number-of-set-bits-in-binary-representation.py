class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n == 1:
                return False
            
            for i in range(2,int(math.sqrt(n))+1):
                if n % i == 0: 
                    return False
            return True
        
        def set_bits(n):
            bits = 0
            while n:
                if n & 1:
                    bits += 1
                n = n >> 1
            return bits
        answer = 0
        for i in range(left, right+1):
            if is_prime(set_bits(i)):
                answer += 1
        return answer
                