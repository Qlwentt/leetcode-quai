from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = set()
        nums.sort()
        
        for i, num in enumerate(nums):
            lo = i + 1
            hi = len(nums) - 1
            while hi > lo:
                threeSum = num + nums[lo] + nums[hi]
                if threeSum > 0:
                    hi -= 1
                elif threeSum < 0:
                    lo += 1
                else: # threeSum == 0
                    solution.add((num, nums[lo], nums[hi]))
                    hi -= 1
                    lo += 1

        return solution
# O(n^2) time
# O(n) space

# alternative solution without Sorting
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         solution = set()
#         dups = set()
#         numsDict = {} 
#         for i, num1 in enumerate(nums):
#             if num1 in dups:
#                 continue
#             dups.add(num1)
#             for j in range(i+1, len(nums)):
#                 num2 = nums[j]
#                 complement = -num1 - num2
#                 if numsDict.get(complement,-1) == i:
#                     solution.add(tuple(sorted([num1,num2,complement])))
#                 numsDict[num2] = i
#         return solution

# O(n^2) time
# O(n) space