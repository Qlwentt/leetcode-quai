class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        @cache
        def isPrime(num):
            if num <= 1:
                return False
            for i in range(2, int(math.sqrt(num)+1)):
                if num % i == 0:
                    return False
            return True
        
        ROWS = len(nums)
        COLS = len(nums[0])
        answer = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if r == c or r+c == ROWS-1 :
                    if isPrime(nums[r][c]):
                        answer = max(nums[r][c], answer)
                        
        return answer
        