class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        p1 = 0
        p2 = n
        
        while p2 < len(nums):
            output.append(nums[p1])
            output.append(nums[p2])
            p1 += 1
            p2 += 1
            
        return output