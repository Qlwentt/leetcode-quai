class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformations = set()
        for word in words:
            transformation = []
            for char in word:
                transformation.append(alphabet[ord(char) - ord("a")])
            transformations.add("".join(transformation))
            
        return len(transformations)