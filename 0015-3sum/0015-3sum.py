class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        for i in range(len(nums)):
            a = nums[i]
            lo = i + 1
            hi = len(nums) - 1
            
            while lo < hi:
                b = nums[lo]
                c = nums[hi]
                if a + b + c > 0: # too high
                    hi -= 1
                elif a + b + c < 0:
                    lo += 1
                else:
                    answer.add(tuple(sorted(([a,b,c]))))
                    lo += 1
                    hi -= 1
        return answer
                            
        