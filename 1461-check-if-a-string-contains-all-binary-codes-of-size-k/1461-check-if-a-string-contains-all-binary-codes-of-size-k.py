from collections import deque
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        code = deque([])
        uniqueCodes = set()
        L = 0
        for R in range(len(s)):
            code.append(s[R])
            if R-L+1 == k:
                uniqueCodes.add("".join(code))
                code.popleft()
                L+=1
        return len(uniqueCodes) == 2 ** k