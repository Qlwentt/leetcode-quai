class Solution:
    def minFlips(self, target: str) -> int:
        flips = len([(k,group) for k, group in itertools.groupby(target)])
        if target[0] == "1":
            return flips
        return flips - 1
            
        