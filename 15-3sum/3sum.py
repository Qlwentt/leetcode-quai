class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # answer = set()
        # nums.sort()
        # target = 0
        # for i in range(len(nums)):
        #     lo = i + 1
        #     hi = len(nums) -1
        #     a = nums[i]
        #     while lo < hi:
        #         if a + nums[lo] + nums[hi] < target:
        #             # too small, increase sum
        #             lo += 1
        #         elif a + nums[lo] + nums[hi] > target:
        #             # too large, decrase sum
        #             hi -= 1
        #         else:
        #             # equals target
        #             answer.add(tuple([a, nums[lo], nums[hi]]))
        #             lo += 1
        #             hi -= 1
        # return answer

        answer = []
        nums.sort()
        target = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                b = nums[lo]
                c = nums[hi]
                if a + b + c > target:
                    hi -= 1
                elif a + b + c < target:
                    lo += 1
                else:
                    answer.append([a,b,c])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
        return answer 


    
# Time: O(N^2)
# Space: O(N) if you count the answer O(1) if you don't