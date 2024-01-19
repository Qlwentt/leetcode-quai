class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        palis = {}
        for bitmap in range(1,2**n):
            subseq = ""
            mask = 1
            for i in range(n):
                # if bit is set, add that letter
                if bitmap & mask:
                    subseq += s[i]
                mask = mask << 1
            # if it is a palindrome, add it to palis
            if subseq == subseq[::-1]:
                palis[bitmap] = len(subseq)
                
        # for each bitmap, check if every other bitmap is disjoint
        # if so record prod of lengths and keep track of max
        answer = 0
        for bmap1 in palis:
            for bmap2 in palis:
                if bmap1 & bmap2 == 0: # none of the bits are 1 in the same position -- disjoint
                    answer = max(answer, palis[bmap1] * palis[bmap2])
                    
        return answer
    
    # Time: 2*2^n
    # space: 2^n
    
    # Had to look up answer on neetcode