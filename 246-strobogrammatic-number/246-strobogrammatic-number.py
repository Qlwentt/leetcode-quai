class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobo = {
            "0" : "0",
            "1" : "1",
            "2" : False,
            "3" : False,
            "4" : False,
            "5" : False,
            "6" : "9",
            "7" : False,
            "8" : "8",
            "9" : "6"
        }
        p1 = 0
        p2 = len(num) -1
        
        while p2 >= p1:
            if not (strobo[num[p1]] and strobo[num[p2]]):
                return False
            if not (strobo[num[p1]] == num[p2] and strobo[num[p2]] == num[p1]):
                return False
            p1 += 1
            p2 -= 1
        return True