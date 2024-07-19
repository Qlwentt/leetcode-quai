class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

#         nums.sort()
#         answer = set()
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 a = nums[i]
#                 b = nums[j]
#                 lo = j+1
#                 hi = len(nums) - 1
                
#                 while lo < hi:
#                     if a + b + nums[lo] + nums[hi] > target:
#                         hi -= 1
#                     elif a + b + nums[lo] + nums[hi] < target:
#                         lo += 1
#                     else:
#                         answer.add(tuple([a,b,nums[lo], nums[hi]]))
#                         lo += 1
#                         hi -= 1
                               
#         return answer

        def kSum(k, target, arr):
            answers = set()
            if k == 2:
                return twoSumII(target, arr)
            else:
                for i in range(len(arr)):
                    a = arr[i]
                    kminus1Answers = kSum(k-1, target-a, arr[i+1:])
                    for answer in kminus1Answers:
                        answer = list(answer)
                        answers.add(tuple([a]+ answer))
                        
            return answers
            
        def twoSumII(target, nums):
            lo = 0
            hi = len(nums) - 1
            answer = set()
            
            while lo < hi:
                if nums[lo] + nums[hi] > target:
                    hi -= 1
                elif nums[lo] + nums[hi] < target:
                    lo += 1
                else:
                    answer.add(tuple([nums[lo], nums[hi]]))
                    lo += 1
                    hi -= 1
            return answer
        nums.sort()
        return kSum(4, target, nums)
        