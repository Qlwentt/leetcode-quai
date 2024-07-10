class Solution:
    def minimumSteps(self, s: str) -> int:
        count_ones = 0
        swaps = 0
        for char in s:
            if char == "0":
                swaps += count_ones
            else:
                count_ones += 1
        return swaps
                