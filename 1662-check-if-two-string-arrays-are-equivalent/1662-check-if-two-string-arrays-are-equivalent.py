class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str_i_1 = 0
        str_i_2 = 0
        
        char_i_1 = 0
        char_i_2 = 0
        
        while True:
            char1 = word1[str_i_1][char_i_1]
            char2 = word2[str_i_2][char_i_2]
            
            if char1 != char2:
                return False
            
            char_i_1 += 1
            char_i_2 += 1
            
            if char_i_1 == len(word1[str_i_1]):
                str_i_1 += 1
                char_i_1 = 0
            
            if char_i_2 == len(word2[str_i_2]):
                str_i_2 += 1
                char_i_2 = 0
            
            if str_i_1 == len(word1) and str_i_2 == len(word2):
                break
            elif str_i_1 == len(word1) or str_i_2 == len(word2):
                return False
            
        return True
    
    # Time: O(N+M)
    # Space: O(1)
        
        