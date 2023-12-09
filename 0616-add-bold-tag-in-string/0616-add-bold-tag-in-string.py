class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        isBold = [False] * (len(s))
        for word in words:
            start = s.find(word)
            end = start + len(word)
            
            while start != -1:
                for i in range(start, end):
                    isBold[i] = True
                
                start = s.find(word, start+1)
                end = start + len(word) 

        answer = []
        i = 0
        while i < len(s):
            if isBold[i]:
                answer.append("<b>")
                while i < len(s) and isBold[i]:
                    answer.append(s[i])
                    i += 1
                answer.append("</b>")
            else:
                answer.append(s[i])
                i+=1
                
        return "".join(answer)
            
    