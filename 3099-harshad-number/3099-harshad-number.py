class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_of_digits = 0
        n = x
        while n:
            sum_of_digits += n % 10
            n //= 10
            
        return sum_of_digits if x % sum_of_digits  == 0 else -1 