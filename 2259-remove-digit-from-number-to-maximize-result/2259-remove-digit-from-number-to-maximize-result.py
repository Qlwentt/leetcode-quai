class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        numbers = []
        for i, curDigit in enumerate(number):
            if curDigit == digit:
                numbers.append(int(number[:i] + number[i+1:]))
        
        return str(max(numbers))
            