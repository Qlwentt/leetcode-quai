class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ones_bit = collections.defaultdict(set)
        freq = []
        for num in candidates:
            x = num
            i = 0
            while x:
                if x & 1:
                    ones_bit[num].add(i)
                    freq.append(i)
                i += 1
                x = x >> 1
        counts = collections.Counter(freq)
        return counts.most_common(1)[0][1]
        
                
        
        
        
        
      
        
        