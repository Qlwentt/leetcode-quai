class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        digitToIndex = {}
        for i, digit in enumerate(num):
            digitToIndex[digit] = i
        
        for i, digit in enumerate(num):
            for potentialSwap in range(9, int(digit), -1):
                d = str(potentialSwap)
                if d in digitToIndex and digitToIndex[d] > i:
                    j = digitToIndex[d]
                    num[i], num[j] = num[j], num[i]
                    return int("".join(num))
        return int("".join(num))
        