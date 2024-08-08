class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_s1 = collections.Counter(s1)
        counts_s2 = collections.defaultdict(int) 
        
        # "dcda"
        #   L
        #    R
        l = 0
        for r in range(len(s2)):
            counts_s2[s2[r]] += 1
            while any(item2 not in counts_s1 for item2 in counts_s2) or any(counts_s2[item2] > counts_s1[item2] for item2 in counts_s2):
                counts_s2[s2[l]] -= 1
                if counts_s2[s2[l]] == 0:
                    del counts_s2[s2[l]]
                l += 1
                    
            if counts_s2 == counts_s1:
                return True
        return False
                
            