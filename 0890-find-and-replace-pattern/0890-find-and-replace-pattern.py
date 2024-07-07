class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        answer = []
        for word in words:
            letter_map = {}
            valid = True
            for i,char in enumerate(word):
                if pattern[i] in letter_map and letter_map[pattern[i]] != char:
                    valid = False
                    break
                letter_map[pattern[i]] = char
            if len(letter_map.values()) != len(set(letter_map.values())):
                valid = False
            if valid:
                answer.append(word)
        return answer
                
            
                
            