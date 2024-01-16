class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
    #   [1, 7, 3, 6, 5, 6 ]
# right [27,20,17,11,6, 0 ]
# left  [0, 1, 8, 11,17,22]

#       [2,1,-1]
# right [0 -1 0]
# left  [0, 1 0]

        rightSums = [0]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            rightSums[i] = nums[i+1] + rightSums[i+1]

        leftSums = [0]*len(nums)
        for i in range(1, len(nums)):
            leftSums[i] = nums[i-1] + leftSums[i-1]

        for i in range(len(nums)):
            if leftSums[i] == rightSums[i]:
                return i

        return -1