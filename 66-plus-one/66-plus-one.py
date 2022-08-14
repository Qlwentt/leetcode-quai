class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strDigits = [str(digit) for digit in digits]
        number = int("".join(strDigits))
        number += 1
        
        number = str(number)
        return [int(digit) for digit in number]