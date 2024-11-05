class Solution:
    def minChanges(self, s: str) -> int:
        curr_length = 0
        changes = 0
        prev = None
        
        for char in s:
            if prev != None and char != prev:
                if curr_length % 2 != 0:
                    changes += 1
                    curr_length += 1
                else:
                    curr_length = 1
            else:
                curr_length += 1
            prev = char
            
        return changes
        
        