class Solution:
    def maximumSwap(self, num: int) -> int:
        numToI = {}
        
        num = list(str(num))
        
        for i, digit in enumerate(num):
            numToI[digit] = i
        
        for i, digit in enumerate(num):
            for greaterDigit in range(9, int(digit), -1):
                d = str(greaterDigit)
                if d in numToI and numToI[d] > i:
                    j = numToI[d]
                    num[i], num[j] = num[j], num[i]
                    return int("".join(num))
        
        return int("".join(num))
                    
        