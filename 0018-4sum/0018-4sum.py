class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
# Iterative only 4 sum
        nums.sort()
        answer = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a = nums[i]
                b = nums[j]
                lo = j+1
                hi = len(nums) - 1
                
                while lo < hi:
                    if a + b + nums[lo] + nums[hi] > target:
                        hi -= 1
                    elif a + b + nums[lo] + nums[hi] < target:
                        lo += 1
                    else:
                        answer.add(tuple([a,b,nums[lo], nums[hi]]))
                        lo += 1
                        hi -= 1
                               
        return answer

# Recursive, k sum:
        def kSum(k, target, arr):
            answers = []
            if k == 2:
                return twoSumII(target, arr)
            else:
                for i in range(len(arr)):
                    a = arr[i]
                    if i > 0 and arr[i] == arr[i-1]:
                        continue
                    kminus1Answers = kSum(k-1, target-a, arr[i+1:])
                    for answer in kminus1Answers:
                        answer.append(a)
                        answers.append(answer)
                        
            return answers
            
        def twoSumII(target, nums):
            lo = 0
            hi = len(nums) - 1
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
        return kSum(4, target, nums)
        