class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        nMinusOne = self.countAndSay(n-1)
        answer = []
        prev = None
        count = 1
        for item in nMinusOne:
            if prev != None:
                if prev == item:
                    count += 1
                else:
                    answer.append(str(count) + prev)
                    count = 1
            prev = item
        answer.append(str(count) + prev)
        return "".join(answer)
    
                    
        