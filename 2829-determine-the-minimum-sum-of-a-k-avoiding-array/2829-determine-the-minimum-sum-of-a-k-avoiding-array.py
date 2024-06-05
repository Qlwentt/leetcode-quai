class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        numSet = set()
        
        i = 1
        count = 0
        curSum = 0
        while count != n:
            if k - i not in numSet:
                curSum += i
                count += 1
                numSet.add(i)
            i += 1
        return curSum