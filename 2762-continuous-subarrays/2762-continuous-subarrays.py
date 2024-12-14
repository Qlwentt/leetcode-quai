from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        answer = 0
        L = 0
        sorted_window = SortedList()
        for R in range(len(nums)):
            sorted_window.add(nums[R])
            while abs(sorted_window[0] - sorted_window[-1]) > 2:
                sorted_window.remove(nums[L])
                L += 1
            answer += (R - L + 1)
        return answer
            
        