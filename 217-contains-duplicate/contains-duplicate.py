class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # # set loop solution
        # nums_set = set()
        # for num in nums:
        #     if num in nums_set:
        #         return True
        #     nums_set.add(num)
        # return False
        # # Time: O(N)
        # # Space: O(N)

        # # one liner
        # return len(set(nums)) != len(nums)
        # # Time: O(N)
        # # Space: O(N)

        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

