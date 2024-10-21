class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        answer = 1
        
        def max_split(i, cur_string, substrings):
            nonlocal answer
            if i == len(s):
                if len(substrings) == len(set(substrings)):
                    answer = max(answer, len(substrings))
                return 
            # take
            
            if substrings:
                new = cur_string + s[i]
                old = substrings[-1]
                substrings[-1] = new
                max_split(i+1, new, substrings)
                substrings[-1] = old
            
            # new string
            
            substrings.append(s[i])
            max_split(i+1, s[i], substrings)
            substrings.pop()
                
        max_split(0, "", [])
        return answer
    # ["a"]
    # [(0,"")(1,'a')]
    
    "www z f v e d w fv h s ww"
     
            
        