class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        [-2, -1, 0, 0, 1, 2]
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