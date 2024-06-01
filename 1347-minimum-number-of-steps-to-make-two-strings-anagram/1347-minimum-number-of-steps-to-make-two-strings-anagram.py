class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countsS = collections.Counter(s)
        countsT = collections.Counter(t)
        
        differences = 0
        uniques = set(list(countsS.keys()) + list(countsT.keys()))
        for char in uniques:
            differences += abs(countsS[char] - countsT[char])
            
        
            
        return differences // 2
        