class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        nMinus1 = self.countAndSay(n-1)
        count = 0
        prev = None
        answer = []
        for item in nMinus1:
            if prev != None and item != prev:
                answer.append(str(count)+ prev)
                count = 1
            else:
                count += 1
            prev = item
        answer.append(str(count)+ prev)
        return "".join(answer)
        