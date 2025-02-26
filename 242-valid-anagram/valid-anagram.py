from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # dictionary solution 

        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}

        for char_s, char_t in zip(s,t):
            count_s[char_s] = count_s.get(char_s, 0) + 1
            count_t[char_t] = count_t.get(char_t, 0) + 1

        # return count_s == count_t (not allowed in certain languages like js)
        
        for char_s in s:
            if count_s.get(char_s, 0) != count_t.get(char_s, 0):
                return False
        return True
        
        # one liner
        return Counter(s) == Counter(t)

# Time: O(N)
# Space: O(N)


        