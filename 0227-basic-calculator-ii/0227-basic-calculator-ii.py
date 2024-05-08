import re
class Solution:
    def calculate(self, s: str) -> int:
        def getNextNumber(j):
            nextNumber = 0
            while j < len(s) and s[j].isdigit():
                nextNumber = nextNumber * 10 + int(s[j])
                j += 1
            return  (nextNumber, j)
        s = s.replace(" ", "")
        
        answer = 0
        i = 0
        lastNumber = 0
        while i < len(s):
            item = s[i]
            if item == "+":
                answer += lastNumber
                nextNumber, newI = getNextNumber(i+1)  
                lastNumber = nextNumber
                print(nextNumber, newI)
                i = newI
            elif item == "-":
                answer += lastNumber
                nextNumber, newI = getNextNumber(i+1)
                lastNumber = nextNumber * -1
                i = newI
            elif item == "*":
                a = lastNumber
                b, newI = getNextNumber(i+1)
                lastNumber = a *b
                i = newI
            elif item == "/":
                a = lastNumber
                b, newI = getNextNumber(i+1)
                lastNumber = int(a/b)
                i = newI
            else:
                lastNumber = lastNumber * 10 + int(item)
                i += 1
        
        answer += lastNumber
            
        return answer
                
                
        