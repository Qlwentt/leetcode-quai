class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        numToI = {digit: i for i, digit in enumerate(num)}
        
        for i, digit in enumerate(num):
            for newDigit in range(9,int(digit), -1):
                if str(newDigit) in numToI:
                    j = numToI[str(newDigit)]
                    if j > i:
                        num[i], num[j] = num[j], num[i]
                        return int("".join(num))
        return int("".join(num))
        
        