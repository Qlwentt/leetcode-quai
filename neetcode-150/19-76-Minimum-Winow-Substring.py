from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countsT = Counter(t)
        
        have = 0
        need = len(countsT)
        
        start = 0
        end = 0
        
        countsS = {}
        
        answer = [-1,-1]
        minLength = float('inf')

        while end < len(s):
            char = s[end]
            if char not in countsT:
                end += 1
                continue

            countsS[char] = countsS.get(char,0) + 1
            if countsS[char] == countsT[char]:
                have += 1
            while have == need:
                windowLength = end - start + 1
                minLength = min(minLength, windowLength)
                if minLength == windowLength:
                    answer = [start,end]
                
                # remove start char from window
                charS = s[start]
                if charS not in countsS:
                    start += 1
                    continue
    
                countsS[charS] -= 1
                if countsS[charS] < countsT[charS]:
                    have -= 1
                start +=1
    
            end += 1

        start, end = answer

        return s[start:end+1] if minLength != float('inf') else ""