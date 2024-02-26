class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        nMinus1 = self.countAndSay(n-1)
        
        answer = []
        prev = None
        count = 0
        for i in range(len(nMinus1)):
            if prev and prev != nMinus1[i]:
                answer.append(str(count)+ prev)
                count = 1
            else:
                count += 1
            prev = nMinus1[i]
        answer.append(str(count)+prev)
        return "".join(answer)
        