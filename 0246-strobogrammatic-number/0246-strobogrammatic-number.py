class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobo = {
            '6': '9',
            '9': '6',
            '8': '8',
            '1': '1',
            '0': '0'
        }
        L = 0
        R = len(num) -1 
        
        while L <= R:
            if strobo.get(num[L], None) != num[R] or  strobo.get(num[R], None) != num[L]:
                return False
            L += 1
            R -= 1
        return True