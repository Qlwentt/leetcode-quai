class Solution:
    def triangleType(self, nums: List[int]) -> str:
        counts = collections.Counter(nums)
        a, b, c = nums
        if a + b <= c or b+ c <= a or a+c <= b:
            return "none"
        if len(counts) == 1:
            return "equilateral"
        if len(counts) == 2:
            return "isosceles"
        return "scalene"
        