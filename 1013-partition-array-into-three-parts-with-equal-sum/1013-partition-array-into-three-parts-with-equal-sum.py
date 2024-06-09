class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum_ = sum(arr)
        if sum_ % 3 != 0:
            return False
        target = sum_ // 3
        curSum = 0
        count = 0
        for R in range(len(arr)):
            curSum += arr[R]
            if curSum == target:
                curSum = 0
                count += 1
                if count == 2 and R != len(arr) -1:
                    return True
        return False