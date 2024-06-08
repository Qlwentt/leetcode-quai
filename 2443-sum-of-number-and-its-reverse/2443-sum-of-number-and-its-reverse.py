class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if not num:
            return True
        
        for x in range(1,num):
            if x + int(str(x)[::-1]) == num:
                return True
            
        return False
            
                