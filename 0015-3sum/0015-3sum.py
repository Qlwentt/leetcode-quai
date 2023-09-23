class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        
        nums.sort()
        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                if nums[low] + nums[high] + nums[i] > 0:
                    high -= 1
                elif nums[low] + nums[high] + nums[i] < 0:
                    low += 1
                else:
                    tup = (nums[low], nums[high], nums[i])
                    result.add(tup)
                    low += 1
                    high -= 1
                    
        return result


            
        