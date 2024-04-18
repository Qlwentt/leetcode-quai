from itertools import groupby
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        nMinus1 = self.countAndSay(n-1)
        answer = [str(len(list(group))) + k for k, group in groupby(nMinus1)]
        return "".join(answer)