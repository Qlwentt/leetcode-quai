class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = set()
        nums.sort()
        for i in range(len(nums)):
            a = nums[i]
            L = i + 1
            R = len(nums) -1 
            while L < R:
                b = nums[L]
                c = nums[R]
                if a + b + c > 0:
                    R -= 1
                elif a + b + c < 0:
                    L += 1
                else:
                    answers.add(tuple(sorted([a,b,c])))
                    L += 1
                    R -= 1
        return answers
        