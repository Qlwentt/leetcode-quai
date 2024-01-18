import re
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = []
        for s in strs:
            encoded.append(str(len(s))+"#"+ s)
        
        return "".join(encoded)
        
# ["Hello","World", "25#Fun"]
      #  "25#Hello5#World6#25Fun" 2+5
      #     P               
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        p = 0
        curLen = ""
        words = []
        while p < len(s):
            char = s[p]
            if char.isdigit():
                curLen += char
                p += 1
            elif char == "#":
                curLen = int(curLen)
                word = s[p+1:p+1+curLen]
                words.append(word)
                p += curLen + 1
                curLen = ""
        return words
        
        
                           
                           
                          
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))