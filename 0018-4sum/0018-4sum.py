class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         # Iterative only 4 sum
#         nums.sort()
#         answer = []
#         for i in range(len(nums)):
#             a = nums[i]
#             if i > 0 and a == nums[i-1]:
#                 continue
#             for j in range(i+1, len(nums)):
#                 if j > i+1 and nums[j] == nums[j-1]:
#                     continue
#                 b = nums[j]
#                 lo = j+1
#                 hi = len(nums) - 1
                
#                 while lo < hi:
#                     if a + b + nums[lo] + nums[hi] > target:
#                         hi -= 1
#                     elif a + b + nums[lo] + nums[hi] < target:
#                         lo += 1
#                     else:
#                         answer.append([a,b,nums[lo], nums[hi]])
                        
#                         lo += 1
#                         hi -= 1
#                         while lo < hi and nums[lo] == nums[lo-1]:
#                             lo += 1
        
#         return answer

# # Recursive, k sum:
        def kSum(k, target, lo, hi):
            answers = []
            if k == 2:
                return twoSumII(target, lo, hi)
            else:
                for i in range(lo, len(nums)):
                    a = nums[i]
                    if i > lo and nums[i] == nums[i-1]:
                        continue
                    kminus1Answers = kSum(k-1, target-a, i+1, hi)
                    for answer in kminus1Answers:
                        answers.append([a]+answer)
                        
            return answers
            
        def twoSumII(target, lo, hi):
            answer = []
            
            while lo < hi:
                if nums[lo] + nums[hi] > target:
                    hi -= 1
                elif nums[lo] + nums[hi] < target:
                    lo += 1
                else:
                    answer.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and lo > 0 and nums[lo] == nums[lo-1]:
                        lo += 1
            return answer
        nums.sort()
        return kSum(4, target, 0, len(nums)-1)
        