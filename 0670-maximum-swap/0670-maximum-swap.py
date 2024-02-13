class Solution:
    def maximumSwap(self, num: int) -> int:
        numDict = {}
        answer = list(str(num))
        for i, n in enumerate(str(num)):
            numDict[n] = i
            
        for i, digit in enumerate(str(num)):
            for higherNum in range(9, int(digit), -1):
                s = str(higherNum)
                if s in numDict and numDict[s] > i:
                    answer[i], answer[numDict[s]] = answer[numDict[s]], answer[i]
                    return int("".join(answer))
                
        return int("".join(answer))
        