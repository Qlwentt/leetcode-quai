class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        pointer1 = 0
        pointer2 = 0

        while pointer1 < len(word1) and pointer2 < len(word2):
            answer.append(word1[pointer1])
            answer.append(word2[pointer2])
            pointer1 += 1
            pointer2 += 1
        
        while pointer1 < len(word1):
            answer.append(word1[pointer1])
            pointer1 += 1

        while pointer2 < len(word2):
            answer.append(word2[pointer2])
            pointer2 += 1
        
        return "".join(answer)
    
    # Time: O(N+M)
    # Space: O(1) (not counting answer)