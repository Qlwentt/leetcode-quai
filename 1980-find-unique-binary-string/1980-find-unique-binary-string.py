class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set([int(num,2) for num in nums])
        n = len(nums)
        
        for i in range(2**n):
            if i not in nums:
                binary = bin(i)[2:]
                return "".join(["0"] * (n - len(binary))) + binary