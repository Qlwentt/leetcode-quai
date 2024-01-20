from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def customSort(a,b):
            if int(str(a)+str(b)) > int(str(b)+str(a)):
                return 1
            elif int(str(a)+str(b)) == int(str(b)+str(a)):
                return 0
            else:
                return -1
        
        nums.sort(key=cmp_to_key(customSort), reverse=True)
        return str(int("".join([str(num) for num in nums])))
    
    
        