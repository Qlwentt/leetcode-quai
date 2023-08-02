class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # answer = set()
        # for i in range(len(nums)):
        #     target = 0 - nums[i]
        #     restOfArray = nums[:i]+nums[i+1:]
        #     complements = set()
        #     for num in restOfArray:
        #         if target - num in complements:            
        #             ele = [nums[i], num, target - num]
        #             ele.sort()
        #             answer.add(tuple(ele))
        #         complements.add(num)
        # return answer
        nums.sort()
        answer = set()
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                currentSum = nums[lo] + nums[hi] + nums[i]
                if currentSum > 0:
                    hi -= 1
                elif currentSum < 0:
                    lo += 1
                else: # currentSum == 0
                    answer.add((nums[lo], nums[hi], nums[i]))
                    lo += 1
                    hi -= 1
        return answer


            
        