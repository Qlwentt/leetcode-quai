class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        #    0     1     2    3    4
        # ["aba","bcb","ece","aa","e"]
        #    1     1     2     3   4
        
        prefix_count = [0]*len(words)
        count = 0
        for i, word in enumerate(words):
            if word[0] in "aeiou" and word[-1] in "aeiou":
                count += 1
            prefix_count[i] = count
        prefix_count = [0] + prefix_count

        answer = []
        for l, r in queries:
            answer.append(prefix_count[r+1]-prefix_count[l])
        return answer 

 
    
           