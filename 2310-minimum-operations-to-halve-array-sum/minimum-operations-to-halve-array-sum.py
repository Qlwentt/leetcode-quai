class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        target = total / 2
        nums = [-num for num in nums]
        heapq.heapify(nums)
        current = 0
        steps = 0
        while current < target:
            greatest = (heapq.heappop(nums) * -1) / 2
            current += greatest
            heapq.heappush(nums, -greatest)
            steps += 1
        return steps

