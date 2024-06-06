class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set([int(num,2) for num in nums])
        n = len(nums)
        
        print(nums)
        for i in range(2**n):
            if i not in nums:
                binary = bin(i)[2:]
                return "".join(["0"] * (n - len(binary))) + binary
        
        # 000, 001, 010, 011, 100, 101, 110, 111
        #  0    1    2    3    4